FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk add libpq-dev python3-dev postgresql postgresql-dev

RUN apk add libc-dev

RUN pip install --upgrade pip && pip install setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "3" , "--loop" ,"uvloop"]

