FROM python:3.7-alpine

COPY bot/config.py /app/
COPY bot/main.py /app/
COPY requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
CMD ["python3", "main.py"]