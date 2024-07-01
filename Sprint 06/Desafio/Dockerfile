
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY movies.csv /app/movies.csv

COPY series.csv /app/series.csv

COPY ingestao_batch_s3.py .

CMD ["python", "ingestao_batch_s3.py"]

