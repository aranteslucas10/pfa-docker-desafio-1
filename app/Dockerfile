FROM python:3.7

RUN apt update

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

ENV FLASK_APP=app.py
ENV DB_DATABASE=desafio1
ENV DB_HOST=pfa-desafio-1-mysql
ENV DB_USER=root
ENV DB_PASSWD=root

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]