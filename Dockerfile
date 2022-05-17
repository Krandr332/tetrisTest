FROM python:3.10

ENV PYTHONDONTWHRITEBYTECODE 1

ENV PYTHONUMBUFFERED 1
WORKDIR /Documents/GitHub/tetrisTest

COPY requirements.txt ./requirements.txt
RUN pip install -r /Documents/GitHub/tetrisTest/requirements.txt

COPY . /Documents/GitHub/tetrisTest
EXPOSE 8000
CMD [ "python", "manage.py","migrate" ]
CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]