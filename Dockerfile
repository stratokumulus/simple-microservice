FROM python:3.10

ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
# The following is only used to create myself a cozy debugging env. Not needed for usual stuff ... !
RUN apt-get update
RUN apt-get install busybox
RUN apt-get -y install iputils-ping
RUN apt-get -y install dnsutils

CMD ["python","micro.py"]
