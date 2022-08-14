ARG BUILD_FROM
FROM $BUILD_FROM

# Set env
ENV GROTT_VERSION '2.6.1'

RUN set -x \
  && pip3 install paho-mqtt requests crudini \
  && apk add --no-cache --virtual .build-dependencies \ 
    git \
  && git clone --depth=1 https://github.com/johanmeijer/grott.git /opt \
  && apk del .build-dependencies

# Copy root filesystem
COPY rootfs /
COPY config.ini /opt

# Sets working directory
WORKDIR /opt