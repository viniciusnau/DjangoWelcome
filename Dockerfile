FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /DjangoWelcome

WORKDIR /DjangoWelcome

ADD . /DjangoWelcome/

RUN make setup-dev