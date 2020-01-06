FROM python:3.7

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  supervisor

RUN mkdir -p /var/log/supervisor && \
  mkdir -p /etc/supervisor/conf.d

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en

ADD . /app

RUN rasa train
EXPOSE 5005 5055

ADD supervisor.conf /etc/supervisor.conf
CMD ["supervisord", "-c", "/etc/supervisor.conf"]
