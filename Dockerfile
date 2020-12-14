FROM python:3.8.6-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt \
    --default-timeout=1000  # a safeguard against slow connections
COPY weather_app ./weather_app
EXPOSE 5000
CMD export FLASK_APP="weather_app" && \
    export FLASK_ENV=development && \
    export DEPLOY=local && \
    flask run --host=0.0.0.0
