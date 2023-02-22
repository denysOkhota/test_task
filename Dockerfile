FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask","run","--port","5000","--host","0.0.0.0"]
