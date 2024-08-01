FROM ubuntu:latest

WORKDIR /

COPY . .

ARG PYTHON_VERSION=3.10

RUN apt update && apt install python3 python3-pip -y
RUN pip3 install -r requirements.txt --break-system-packages

CMD [ "python3", "main.py" ]
