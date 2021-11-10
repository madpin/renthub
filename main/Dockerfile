FROM python:3.8.12-slim-buster

# MAINTANER Thiago MadPin "madpin@gmail.com"



# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY ./alembic.ini /app/alembic.ini

COPY ./app /app

# ENTRYPOINT [ "python" ]

# CMD [ "ddtrace-run", "uvicorn", "main:app",  "--host", "0.0.0.0" ]
CMD ["uvicorn", "main:app",  "--host", "0.0.0.0", "--reload"]
