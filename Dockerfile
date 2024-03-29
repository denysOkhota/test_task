FROM python:3.12.0b1-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask","run","--port","8080","--host","0.0.0.0"]
