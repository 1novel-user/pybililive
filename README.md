# 🚀 BiliLive-Alert 

 **Real-time Bilibili Live Stream Monitoring System | b站开播提醒器**

## ✨ 核心功能

### **监控开播**：监控指定主播的b站直播间，以“双尾彗星”这名主播为例

### **消息通知**：指定主播一旦开播，以电脑端右下角弹窗及微信通知提醒，点击即可进入直播间

## 环境依赖  

### python(无需python的版本正在测试，尽情期待)

### **time、requests、winotify**

## 🌍 应用场景（可能需配合其他工具）

- 主播粉丝：实时接收开播提醒，避免错过精彩内容
- MCN机构：批量监控旗下主播直播状态
- 数据分析：记录直播时长/人气值变化曲线
- 运维监控：直播流稳定性监测报警

## 使用方法

### 1.下载代码、依赖

```shell
pip install time
pip install requests
pip install winotify
```

### 2.修改参数

```python
 ROOM_ID = 1496449 #你要监控的直播间代码
 INTERVAL = 60 #查询时间间隔
 name = "双尾彗星" #你要查询的主播名称
 #通知方式配置
 ENABLE_WECHAT = True # 启用微信提醒
 ENABLE_WIN_TOAST = True  # 启用Windows弹窗
 微信Server酱配置（https://sct.ftqq.com）#请移步server酱获取sckey
 WECHAT_SCKEY = "" #你的SCKEY
```

### 3.后台自启动

(如果不想自启动，可以直接在上一步后把程序挂在idle里面让他运行，如果不想每次开机都要运行一次那么麻烦，可以看以下方式实行开机自启设置：）

### Windows 系统

### 方案一：使用任务计划程序（最稳定）

** 1.创建任务基本属性：  **

 按 Win+R 输入:taskschd.msc  

 右侧操作栏选择:创建基本任务，名称填:直播监控  

 触发器选择:当用户登录时  

** 2.配置操作：  **  

 操作类型选择"启动程序"  

 程序/脚本：C:\你的pythonw地址\pythonw.exe  # 使用pythonw避免弹出黑窗  

 参数："C:\你的代码地址\watch_bili_live.py"  

 起始于：C:\你的代码地址\  

** 3.高级设置(重要):  **

 勾选"使用最高权限运行"  

 条件标签页取消所有勾选  

 设置里选择"如果任务失败，每隔1分钟重启"  

 （建议重启后查看运行状态，如状态显示“准备就绪”，可以把触发器修改成“不管用户是否登录都要运行”）  



### 方案二：启动文件夹（快捷方式）

** 1.创建快捷方式:  **

 在文件资源管理器地址栏输入：shell:startup  

 右键新建快捷方式，目标填写：  

 "C:\你的pythonw路径\pythonw.exe" "C:\你的代码路径\watch_bili_live.py"  

> 附：电脑端实现形式以右下角弹窗方式与一声默认提示音提醒  
>
> 如想实现重复通知，可以把第71行的
> 
>
>```python
>    toast.set_audio(audio.Default, loop=False)
>```
>
> 中"loop=False"中False改为True
> 

# 欢迎大佬批评建议
友情链接：[双尾彗星直播间](https://live.bilibili.com/1496449?live_from=85001&spm_id_from=333.1365.live_users.item.click)
