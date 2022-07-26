FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip python-is-python3
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# RUN apt-get install -y vim less libsndfile1-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY ./script/helloworld.py /usr/local/bin
RUN chmod +x /usr/local/bin/helloworld.py

COPY ./bin/setup /usr/local/bin
RUN chmod +x /usr/local/bin/setup

# CMD [ "setup" ]


