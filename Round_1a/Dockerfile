FROM --platform=linux/amd64 python:3.11-alpine
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache /tmp/*
COPY app/ /app/
ENTRYPOINT ["python", "main.py"]