FROM ubuntu:20.04
ENV TZ=Asia/Tokyo
ENV PULSE_SERVER=docker.for.mac.localhost
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y python3 python3-pip python-is-python3 portaudio19-dev pulseaudio ffmpeg
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN pip install --upgrade pip setuptools
RUN python -m pip install numpy soundfile ffmpeg pyaudio pydub grpcio grpcio-tools watchdog

COPY ./bin/player /usr/local/bin
RUN chmod +x /usr/local/bin/player
COPY ./bin/recorder /usr/local/bin
RUN chmod +x /usr/local/bin/recorder
COPY ./bin/watch /usr/local/bin
RUN chmod +x /usr/local/bin/watch
