FROM python:3.9.10-slim-bullseye
RUN mkdir -p /app/src
RUN mkdir -p /app/data/input
RUN mkdir -p /app/data/output
RUN mkdir -p /app/train_models
WORKDIR /app/src/
COPY  ./requirements.txt /app/src/requirements.txt 
RUN pip install -r requirements.txt
COPY  ./*.py /app/src/
ENTRYPOINT [ "python" ] 
