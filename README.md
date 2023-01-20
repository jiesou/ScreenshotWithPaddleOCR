# Screenshot with PaddleOCR

[中文](/#中文)

One-Click Screenshot OCR Suite for Linux Desktop

Based on [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) and Docker

## Installation

### 0. Clone repository

```
sudo apt install git # Ubuntu/Debian
git clone https://github.com/jiesou/ScreenshotWithPaddleOCR
cd ScreenshotWithPaddleOCR
```

### 1. Dependencies

The script depends on docker, gnome-screenshot, xclip

``sudo apt install docker gnome-screenshot xclip``

### 2. Build the Docker image

`docker build -t paddleocr . `

### 3. Set shortcuts

You can use the GUI to bind scripts to set shortcuts:

![GUI](https://user-images.githubusercontent.com/84175239/213644404-a0762776-e068-423b-861d-e0a37eb381a3.png)

You can also use the command line

The repository comes with a command line script for setting shortcuts in the GNOME environment ([source](https://askubuntu.com/a/597414))

e.g. `python3 set_customshortcut.py 'Screenshot with PaddleOCR' 'bash /path/to/screenshot.sh' '<Super><Shift>t`

## Use

Run screenshot.sh to trigger a screenshot, a notification will be sent when the recognition is done, and the content will be automatically copied to the clipboard

## 中文

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

![GUI](https://user-images.githubusercontent.com/84175239/213644404-a0762776-e068-423b-861d-e0a37eb381a3.png)

你也可以使用命令行

存储库附带了一个设置 GNOME 环境下设置快捷键的命令行脚本（[来源](https://askubuntu.com/a/597414)）

如 `python3 set_customshortcut.py 'Screenshot with PaddleOCR' 'bash /path/to/screenshot.sh' '<Super><Shift>t`

## 使用

运行 screenshot.sh 即触发截图，完成识别后将通知提示，识别内容自动复制到剪切板
