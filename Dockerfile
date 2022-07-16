FROM ubuntu:20.04

COPY .bin/soundcheck_start /usr/local/bin
RUN chmod +x /usr/local/bin/soundcheck_start

CMD [ "soundcheck_start" ]
