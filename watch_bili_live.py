import time
import requests
from winotify import Notification, audio


# ========== 用户配置区域 ==========
ROOM_ID = 1496449
INTERVAL = 60
name = "双尾彗星"

# 通知方式配置
ENABLE_WECHAT = True # 启用微信提醒
ENABLE_WIN_TOAST = True  # 启用Windows弹窗

# 微信Server酱配置（https://sct.ftqq.com）
WECHAT_SCKEY = "" #你的SCKEY

# ================================

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': f'https://live.bilibili.com/{ROOM_ID}'
}


def get_live_status(room_id: int) -> bool:
    """获取直播间状态"""
    url = "https://api.live.bilibili.com/room/v1/Room/get_info"
    try:
        resp = requests.get(url, params={"room_id": room_id}, headers=HEADERS, timeout=10)
        data = resp.json().get("data", {})
        return data.get("live_status", 0) == 1
    except Exception as e:
        print(f"[API请求异常] {str(e)}")
        return False


def send_wechat(title: str, content: str):
    """通过Server酱发送微信通知"""
    if not ENABLE_WECHAT or not WECHAT_SCKEY:
        return

    api_url = f"https://sctapi.ftqq.com/{WECHAT_SCKEY}.send"
    payload = {
        "title": title,
        "desp": content
    }
    try:
        resp = requests.post(api_url, data=payload)
        print(f"[微信通知] 发送状态：{resp.json().get('message', '未知状态')}")
    except Exception as e:
        print(f"[微信通知失败] {str(e)}")


def send_win_toast():
    if not ENABLE_WIN_TOAST:
        return


        # 使用通用点击链接参数
    toast = Notification(
        app_id="B站直播监控",
        title=f"{name}开播啦！",
        msg="点击通知进入直播间",
        duration="long",
        icon=r"https://www.bilibili.com/favicon.ico",
        launch=f"https://live.bilibili.com/{ROOM_ID}"  # 直接集成到通知参数
    )

        # 添加提示音效
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def main():
    print("启动直播检测系统，Ctrl+C退出")
    last_status = False

    try:
        while True:
            current_status = get_live_status(ROOM_ID)

            if current_status and not last_status:
                print("检测到开播！")
                message = f"{name}开始直播啦！\n直播间地址：https://live.bilibili.com/{ROOM_ID}"

                # 发送所有启用通知
                if ENABLE_WIN_TOAST:
                    send_win_toast()
                if ENABLE_WECHAT:
                    send_wechat("直播提醒", message)

            last_status = current_status
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\n监控已停止")


if __name__ == "__main__":
    main()
