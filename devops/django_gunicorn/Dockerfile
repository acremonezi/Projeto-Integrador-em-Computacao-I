FROM python:3.8.10-alpine

RUN pip install --upgrade pip

COPY ./devops/django_gunicorn/requirements.txt .
RUN pip install -r requirements.txt

COPY ./django_project /app
#RUN mkdir -p /app

WORKDIR /app

COPY ./devops/django_gunicorn/entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]