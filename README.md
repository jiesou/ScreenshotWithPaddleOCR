# Screenshot with PaddleOCR

One-Click Screenshot OCR Suite for Linux Desktop

适用于 Linux 桌面环境的一键截图 OCR 套件

基于 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 和 Docker

## 安装

### 0. 克隆存储库

```shell
sudo apt install git # Ubuntu/Debian
git clone https://github.com/jiesou/ScreenshotWithPaddleOCR
cd ScreenshotWithPaddleOCR
```

### 1. 依赖环境

安装 [Docker](https://docs.docker.com/engine/install/)

然后运行

```shell
sudo apt install gnome-screenshot xclip # Ubuntu/Debian
```

建议使用 venv 隔离环境

```shell
python3 -m venv .
source bin/activate
```

### 2. 构建&运行 Docker

运行

```shell
docker build -t paddleocr .
docker run --name paddleocr -idt -v ./app/:/root/ paddleocr
```

### 3. 设置快捷键

你可以使用 GUI 来把脚本绑定到设定的快捷键上：

![GUI](https://user-images.githubusercontent.com/84175239/213644404-a0762776-e068-423b-861d-e0a37eb381a3.png)

你也可以使用命令行

存储库附带了一个设置 GNOME 环境下设置快捷键的命令行脚本（[来源](https://askubuntu.com/a/597414)）

```shell
python3 set_customshortcut.py 'Screenshot with PaddleOCR' 'source /PATH/TO/bin/activate && pythonPATH/TO/screenshot.py
' '<Super><Shift>t'
```

## 使用

```shell
python3 screenshot.py
```

运行 screenshot.py 即触发截图，完成识别后将通知提示，识别内容自动复制到剪切板

### 命令行参数

你可以使用 `-h` 或 `--help` 来查看所有参数的使用说明，即：

```shell
./screenshot.py -h
```

#### 语言

```shell
--lang LANG
```

指定 OCR 识别的语言，可用项参考 [PaddleOCR 文档](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/multi_languages_en.md#5-support-languages-and-abbreviations)。使用新语言时会自动下载对应模型，只要 Docker Container 不被移除模型就不用重新下载

你可以将不同语言绑定到不同快捷键上，例如：
```shell
python3 set_customshortcut.py 'Screenshot with PaddleOCR (Chinese)' 'source /PATH/TO/bin/activate && pythonPATH/TO/screenshot.py -l chi
' '<Super><Shift>t'
python3 set_customshortcut.py 'Screenshot with PaddleOCR (Engilsh)' 'source /PATH/TO/bin/activate && pythonPATH/TO/screenshot.py -l en
' '<Super><Alt>t'
python3 set_customshortcut.py 'Screenshot with PaddleOCR (Japanese)' 'source /PATH/TO/bin/activate && pythonPATH/TO/screenshot.py -l japan
' '<Super><Ctrl>t'
```

### Shell 脚本

你也可使用 Shell 脚本（位于 scripts/screenshot.sh）来触发 OCR 截图，它是对 screenshot.py 在 Shell 的重新实现

会缺失部分功能（如设置语言），某些情况可能没法用 Shell 脚本

这不需要安装 pip 依赖

## 卸载

```shell
sh scripts/uninstall.sh
```

将会自动删除相关处理 OCR 的 Docker 内容，并删除目录

但它不会将你设置的键盘快捷键和本脚本需要的其它依赖移除

如果你要移除相关依赖，可以用包管理器来完成

```shell
sudo apt autoremove --purge gnome-screenshot xclip # Ubuntu/Debian
```

但请注意，其它程序也有可能使用这些依赖，这可能导致其它程序被破坏，甚至系统损坏，**十分危险**。运行前请先确保你知道你在干什么

## 调试

要调试 Docker 中的 Python，你可以使用 VSCode 中的 Docker 插件，参考[文档](https://code.visualstudio.com/docs/containers/overview)

存储库已设置了合适的调试选项，修改在 `.vscode/tasks.json` 中的 `tasks.dockerRun.volumes.localPath` 内容为你本地 volume 的路径（项目根目录）即可

scripts 文件夹中的脚本可能有所帮助，例如

```shell
./scripts/reinstall.sh && python3 screenshot.py
```

就能重新安装并运行 screenshot.py
