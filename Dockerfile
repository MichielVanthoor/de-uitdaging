FROM python:3.6-alpine

RUN adduser -D de-uitdaging

WORKDIR /home/de-uitdaging

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY de-uitdaging.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP de-uitdaging.py

RUN chown -R de-uitdaging:de-uitdaging ./
USER de-uitdaging

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
