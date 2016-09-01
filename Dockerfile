FROM python:2.7
ARG settings
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN apt-get update
RUN apt-get install npm -y
RUN npm install -g bower
RUN apt-get install ruby-dev rubygems -y
RUN gem update --system
RUN gem install compass
RUN ln -s `which nodejs` /usr/bin/node
RUN pip install --upgrade -r requirements.txt

RUN python manage.py bower_install -- --allow-root
RUN python manage.py collectstatic --settings=$settings --noinput
