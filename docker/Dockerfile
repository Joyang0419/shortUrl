FROM python:3.8-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
# RUN mkdir app
WORKDIR /app

COPY ./src/ /app/src
COPY requirements.txt /app
COPY .env /app
COPY jwtRS256.key /app
COPY jwtRS256.key.pub /app
COPY ./alembic/ /app/alembic
COPY alembic.ini /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN alembic upgrade head

CMD ["uvicorn", "src.application:app", "--host", "0.0.0.0", "--port", "9000"]


