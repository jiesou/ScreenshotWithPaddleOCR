#!/usr/bin/env python3
import subprocess
import os, io, tarfile, re, argparse, asyncio

import docker
import pyperclip

# parse args
parser = argparse.ArgumentParser(description="Screenshot with OCR, see https://github.com/jiesou/ScreenshotWithPaddleOCR")
parser.add_argument("-l", "--lang", default="ch", help="set ocr language")
args = parser.parse_args()

def sendNotify(msg):
        subprocess.run(["notify-send", "-e", "OCR", msg])


client = docker.from_env()

# get docker container
if client.containers.list(all=True, filters={'name': 'paddleocr'}):
    container =  client.containers.get('paddleocr')
else:
    sendNotify("Starting docker container...")
    container =  client.containers.run("paddleocr", detach=True, tty=True, name="paddleocr")

if container.status != "running":
    container.start()

temp = "/tmp/temp.png"

# use gnome screenshot to capture image
subprocess.Popen(["gnome-screenshot", "-a", "-f", temp]).communicate()

# tar image to send to docker container
stream = io.BytesIO()
with tarfile.open(fileobj=stream, mode='w') as tar, open(temp, 'rb') as f:
    info = tar.gettarinfo(fileobj=f)
    info.name = os.path.basename(temp)
    tar.addfile(info, f)
try:
    container.put_archive("/app", stream.getvalue())
except AttributeError:
    exit()

# run OCR
result =  container.exec_run(f'python3 -m ocr {args.lang}').output.decode('utf-8')

# copy OCR result to clipboard
pyperclip.copy(re.sub(r"\s*$", r"", result))

sendNotify("Copied to clipboard")

