#!/usr/bin/env python3
import subprocess
import os, io, tarfile, re, argparse

import docker
import pyperclip

# parse args
parser = argparse.ArgumentParser(description="Screenshot with OCR, needn't any arguments")
parser.add_argument("-l", "--lang", default="ch",
    help="OCR Language, see: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/multi_languages_en.md#5-support-languages-and-abbreviations")
args = parser.parse_args()

temp = "/tmp/temp.png"

# use gnome screenshot to capture image
subprocess.run(["gnome-screenshot", "-a", "-f", temp])

client = docker.from_env()

# if container is not running, start it
if not client.containers.list(filters={'name': 'paddleocr'}):
    subprocess.run(["notify-send", "-e", "OCR", "Starting docker container"])
    try:
        client.containers.run("paddleocr", detach=True, tty=True, name="paddleocr")
    except docker.errors.APIError:
        client.containers.get('paddleocr').start()

# get docker container
container = client.containers.get('paddleocr')

# tar image to send to docker container
stream = io.BytesIO()
with tarfile.open(fileobj=stream, mode='w') as tar, open(temp, 'rb') as f:
    info = tar.gettarinfo(fileobj=f)
    info.name = os.path.basename(temp)
    tar.addfile(info, f)
container.put_archive("/app", stream.getvalue())

# run OCR
result = container.exec_run(f'python3 -m ocr {args.lang}').output.decode('utf-8')

# copy OCR result to clipboard
pyperclip.copy(re.sub(r"\s*$", r"", result))

# send notification
subprocess.run(["notify-send", "-e", "OCR", "Copied to clipboard"])