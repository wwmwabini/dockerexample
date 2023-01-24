FROM python:3.10-alpine

RUN apk add py3-pip

WORKDIR /var/www/users

COPY users /var/www/users

RUN pip install -r /var/www/users/requirements.txt

EXPOSE 5025

CMD ["python3", "run.py"]
