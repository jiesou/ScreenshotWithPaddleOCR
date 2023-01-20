#!/bin/bash 
# Dependencies: docker gnome-screenshot xclip

temp=/tmp/temp

gnome-screenshot -a -f $temp.png

# If the docker container is not running, start it.
if  [[ ! $(docker ps -q -f name=^paddleocr$) ]];  then 
    docker run --name paddleocr -idt paddleocr
fi

docker cp $temp.png paddleocr:/app

docker exec -it paddleocr python3 -m ocr  | xclip -i && notify-send -e "OCR" "Copied to clipboard"

exit