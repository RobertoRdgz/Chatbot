FROM python:3.7

WORKDIR /app

ADD . /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5004
WORKDIR /app/src
ENTRYPOINT  ["gunicorn"]
CMD ["-c", "gunicorn.py", "database:app"]
