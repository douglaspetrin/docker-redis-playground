FROM python:3.7-alpine

WORKDIR /src

RUN pip install pipenv

RUN apk add --update mysql mysql-client && rm -f /var/cache/apk/*

EXPOSE 3306

COPY src/Pipfile Pipfile

RUN pipenv install

COPY src/ .

CMD ["pipenv", "run", "python", "main.py"]

