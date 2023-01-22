FROM python:3.10-alpine

RUN apk add py3-pip

WORKDIR /var/www/webapp

COPY . /var/www/webapp

RUN pip install -r requirements.txt

EXPOSE 5024

CMD ["python3", "run.py"]