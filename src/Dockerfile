FROM python:3.9.10-slim-bullseye
RUN mkdir /src/
COPY  ./requirements.txt /src/requirements.txt 
WORKDIR /src/
RUN pip install -r requirements.txt
COPY  ./*.py /src/
ENTRYPOINT [ "python" ] 
