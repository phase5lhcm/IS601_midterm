FROM python:3.10

WORKDIR /app

COPY calculator /app/calculator
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "/app/calculator_proj/main.py"]