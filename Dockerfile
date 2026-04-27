FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV APP_NAME="Cloud Pulse App"
ENV APP_VERSION="1.0.0"
ENV CLOUD_PROVIDER="AWS Cloud"
ENV ENVIRONMENT="production"

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
