FROM python:3.7-alpine

WORKDIR /src

RUN pip install pipenv

COPY src/Pipfile Pipfile

RUN pipenv install

COPY src/ .

CMD ["pipenv", "run", "python", "main.py"]

