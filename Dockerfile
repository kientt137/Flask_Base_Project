FROM python:3.10-buster

ENV TZ=UTC

WORKDIR /usr/src/app

RUN apt-get update
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "-c", "src/Config/gunicorn_hooks_config.py", "--bind=0.0.0.0:5000", "-w", "3", "--worker-class=gevent", "app:app", "--timeout", "600"]