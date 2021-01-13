FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

CMD pip install -r requirements.txt && python manage.py database init && python manage.py database migrate && python manage.py database upgrade &&gunicorn -w4 -b 0.0.0.0:8000 --log-level=debug --access-logfile error.log manage:app

