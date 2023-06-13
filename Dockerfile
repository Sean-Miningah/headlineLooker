FROM python:3.10-slim-buster

# set working directory
WORKDIR /app

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && apt-get install -y gcc

RUN pip install --upgrade pip
RUN apt-get install -y nano

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
EXPOSE 5566

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "config.wsgi:application"]
# CMD ["./start.sh"]