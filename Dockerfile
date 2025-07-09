FROM python:3.10-slim
WORKDIR /app
COPY http_driver.py .
EXPOSE 5000
CMD ["python", "http_driver.py"]
