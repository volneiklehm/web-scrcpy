# Web-scrcpy
通过web远程控制Android手机

## 效果展示
![效果展示](./animation.gif)

## 安装指南
1. 安装adb，确保adb在path环境变量中，并且Android设备已连接并启用调试模式
2. 安装Python 3.7+和pip
3. 安装源码：
   - 克隆项目仓库：`git clone https://github.com/baixin1228/web-scrcpy.git`
   - 进入项目目录：`cd web-scrcpy`
   - 安装依赖：`pip3 install -r requirements.txt`
   - 启动运行：`python3 app.py`
4. 打开一个浏览器，访问`http://localhost:5000`，即可看到scrcpy的控制界面

## 命令行选项

| 选项 | 默认值 | 说明 |
|------|--------|------|
| `--video_bit_rate` | `1024000` | 发送给 scrcpy 服务端的视频码率（bps） |
| `--new-display` | _(禁用)_ | 在设备上创建虚拟副屏 |

### `--new-display` — 虚拟副屏（如 Samsung DeX）

部分 Android 设备（例如支持 Samsung DeX 的设备）允许创建独立于物理屏幕的虚拟副屏，等同于在桌面端执行 `scrcpy --new-display=WxH/DPI`。

**支持的格式：**

```bash
# 自动分辨率和 DPI（由设备决定）
python3 app.py --new-display

# 指定分辨率和 DPI
python3 app.py --new-display=1920x1080/284

# 指定分辨率，使用系统默认 DPI
python3 app.py --new-display=1920x1080

# 自动分辨率，仅指定 DPI
python3 app.py --new-display=/284
```

使用该选项时，设备上会创建一个新的虚拟屏幕并在浏览器中镜像显示，不影响物理屏幕。如需镜像物理屏幕（默认行为），省略该选项即可。

> **注意：** 虚拟副屏支持取决于设备。支持 `android.hardware.type.pc`（如 Samsung DeX 模式）或启用了 `FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS` 的设备可以使用此功能。

## 参与方式
1. Fork 项目.
2. 创建一个新分析: git checkout -b your - branch - name
3. 提交Pull Request.

## 开源协议
Apache License 2.0.

## 联系方式
1228504957@qq.com