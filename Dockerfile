FROM python:3.6-slim

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8050

ENV NAME World

CMD ["python", "dashboards/dashboard1.py"]