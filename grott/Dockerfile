ARG BUILD_FROM
FROM $BUILD_FROM

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN set -x \
  && pip install -r requirements.txt \
  && apk add --no-cache --virtual .build-dependencies \ 
    git \
  && git clone --depth=1 https://github.com/johanmeijer/grott.git /opt \
  && apk del .build-dependencies

# Copy root filesystem
COPY rootfs /
COPY config.ini /opt
COPY autodiscovery.py /opt

# Sets working directory
WORKDIR /opt