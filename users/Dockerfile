FROM python:3.10-alpine

RUN apk add py3-pip

COPY users /var/www/users

WORKDIR /var/www/users
users
RUN pip install -r /var/www/users/requirements.txt

CMD ["python3", "run.py"]
