FROM python:3.10-slim-buster

ENV HOME=/srv/app
COPY ./ $HOME

RUN apt-get update
RUN apt-get -y install python3-pyqt5 libsecp256k1-0 python3-cryptography
RUN python3 -m pip install --user $HOME/Electrum-4.3.4.tar.gz
RUN python3 -m pip install pycryptodomex

CMD ["python", "srv/app/main.py"]