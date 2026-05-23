# EN|[中文](README_zh.md)
# Web-scrcpy
allowing you to control your Android device from a web browser. Web server for scrcpy.

## Effect Demonstration
![Effect](./animation.gif)

## Installation Guide
1. Install adb, ensure that adb is in the path environment variable, and the Android device is connected and the debugging mode is enabled.
2. Install Python 3.7+ and pip.
3. Install the source code:
   - Clone the project repository: `git clone https://github.com/baixin1228/web-scrcpy.git`
   - Navigate to the project directory: `cd web-scrcpy`
   - Install the dependencies: `pip3 install -r requirements.txt`
   - Start running: `python3 app.py`
4. Open a browser and visit http://localhost:5000, then you can see the control interface of scrcpy.

## Command-line Options

| Option | Default | Description |
|--------|---------|-------------|
| `--video_bit_rate` | `1024000` | Video bitrate sent to the scrcpy server (bps) |
| `--new-display` | _(disabled)_ | Create a virtual secondary display on the device |

### `--new-display` — Virtual Display (e.g. Samsung DeX)

Some Android devices (such as those supporting Samsung DeX) allow creating a virtual secondary display independent of the physical screen. This is equivalent to running `scrcpy --new-display=WxH/DPI` from the desktop client.

**Accepted formats:**

```bash
# Auto size and DPI (device chooses defaults)
python3 app.py --new-display

# Fixed resolution and DPI
python3 app.py --new-display=1920x1080/284

# Fixed resolution, system default DPI
python3 app.py --new-display=1920x1080

# Auto size, fixed DPI only
python3 app.py --new-display=/284
```

When this option is used, a new virtual display is created on the device and mirrored in the browser. The physical screen is not affected. To mirror the physical screen (default behaviour), simply omit the option.

> **Note:** Virtual display support depends on the device. It works on devices that support `android.hardware.type.pc` (e.g. Samsung DeX mode) or have `FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS` enabled.

## Contributing
1. Fork the repo.
2. Create a new branch: git checkout -b your - branch - name
3. Make changes and submit a Pull Request.

## License
Apache License 2.0.

## Contact
1228504957@qq.com