FROM gcr.io/google-appengine/python
MAINTAINER aromeronavia@gmail.com

ARG PROJECT_DIR=/app
ARG VENV_DIR=.venv

WORKDIR ${PROJECT_DIR}

ADD ./requirements.txt requirements.txt

RUN virtualenv ${VENV_DIR} -p python3.6

ARG BIN_DIR=${VENV_DIR}/bin
ENV BIN_DIR=${BIN_DIR}

RUN ${BIN_DIR}/pip install -r requirements.txt

ADD . .

CMD ./start.sh
