FROM python:3.8

COPY requirements.txt .

RUN apt-get update && apt-get install -y netcat

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

EXPOSE 1337

USER 1000

CMD ["./wait-for-it.sh", "db", "5432", "--", "python", "./server.py"]
