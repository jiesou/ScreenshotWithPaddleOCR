#!/bin/bash

temp=./temp.png

gnome-screenshot -a -f $temp.png

# If the docker container is not running, start it.
if  [[ ! $(docker ps -q -f name=^paddleocr$) ]];  then
    notify-send -e "OCR" "Starting docker container"
    docker run --name paddleocr -idt paddleocr | docker start paddleocr
fi

docker cp $temp paddleocr:/app
docker exec -it paddleocr python3 -m ocr | xclip -sel c

notify-send -e "OCR" "Copied to clipboard"

exit