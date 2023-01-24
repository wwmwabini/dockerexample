FROM python:3.10-alpine

RUN apk add py3-pip

WORKDIR /var/www/register

COPY register /var/www/register

RUN pip install -r /var/www/register/requirements.txt

EXPOSE 5024

CMD ["python3", "run.py"]
