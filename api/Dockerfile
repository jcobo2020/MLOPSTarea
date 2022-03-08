FROM python:3.9.10-slim-bullseye
RUN mkdir -p /app/api
RUN mkdir -p /app/data/output
RUN mkdir -p /app/train_models
WORKDIR /app/api/
COPY  ./requirements.txt /app/api/requirements.txt 
RUN pip install -r requirements.txt
COPY  ./*.py /app/api/
ENTRYPOINT [ "python" ] 