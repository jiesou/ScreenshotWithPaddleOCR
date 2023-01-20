#!/usr/bin/env python3
import subprocess
import os, io, tarfile

import docker
import pyperclip

temp = "/tmp/temp.png"

# use gnome screenshot to capture image
subprocess.run(["gnome-screenshot", "-a", "-f", temp])

client = docker.from_env()

# if container is not running, start it
if not client.containers.list(filters={'name': 'paddleocr'}):
    subprocess.run(["notify-send", "-e", "OCR", "Starting docker container"])
    client.containers.run("paddleocr", detach=True, name="paddleocr")

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
result = container.exec_run('python3 -m ocr')

# copy OCR result to clipboard
pyperclip.copy(result.output.decode('utf-8'))

# send notification
subprocess.run(["notify-send", "-e", "OCR", "Copied to clipboard"])