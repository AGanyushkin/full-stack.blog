FROM python:3

WORKDIR /data

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
