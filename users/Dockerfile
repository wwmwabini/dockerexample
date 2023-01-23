FROM python:3.10-alpine

RUN apk add py3-pip

COPY . /var/www/webapp

WORKDIR /var/www/webapp

RUN pip install -r /var/www/webapp/requirements.txt

CMD ["python3", "run.py"]
