# Screenshot with PaddleOCR

适用于 Linux 桌面环境的一键截图 OCR 套件
基于 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 和 Docker

## 安装

### 0. 克隆存储库

```
sudo apt install git # Ubuntu/Debian
git clone https://github.com/jiesou/ScreenshotWithPaddleOCR
cd ScreenshotWithPaddleOCR
```

### 1. 依赖环境

脚本依赖 docker、gnome-screenshot、xclip

`sudo apt install docker gnome-screenshot xclip`

### 2. 构建 Docker 镜像

`docker build -t paddleocr .`

### 3. 设置快捷键

你可以使用 GUI 来把脚本绑定到设定的快捷键上：

你也可以使用命令行

存储库附带了一个设置 GNOME 环境下设置快捷键的命令行脚本（[来源](https://askubuntu.com/a/597414)）

如 `python3 set_customshortcut.py 'Screenshot with PaddleOCR' 'bash /path/to/screenshot.sh' '<Super><Shift>t`

## 使用

运行 screenshot.sh 即触发截图，完成识别后将通知提示，识别内容自动复制到剪切板
