FROM python:3.10.13-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "app.py"]