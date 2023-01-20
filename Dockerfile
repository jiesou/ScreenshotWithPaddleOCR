FROM registry.baidubce.com/paddlepaddle/paddle:2.4.1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY app /app