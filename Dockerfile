FROM registry.baidubce.com/paddlepaddle/paddle:2.4.1

WORKDIR /app
COPY app /app

RUN python -m pip install -r requirements.txt