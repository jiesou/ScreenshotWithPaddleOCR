docker rm -f paddleocr
docker build --tag paddleocr .
docker run --name paddleocr -idt -v ./app/:/root/ paddleocr
