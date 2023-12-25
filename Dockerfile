FROM debian:buster-slim

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y install python3 python3-pydub sox 

RUN mkdir /output
RUN mkdir /app
ADD . /app
WORKDIR /app

RUN chmod a+rx /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
