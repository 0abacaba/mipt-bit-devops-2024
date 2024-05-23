FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./


RUN pip install --upgrade pip && pip install setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python3","-u","main.py",">>","/shared/statistics.log"]

