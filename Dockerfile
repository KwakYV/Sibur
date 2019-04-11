FROM python:latest
WORKDIR /iiotbackend
COPY requirements.txt /iiotbackend/
RUN pip install -r requirements.txt

