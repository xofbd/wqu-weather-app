FROM python:3.7.2-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD bin/run.sh 0.0.0.0
