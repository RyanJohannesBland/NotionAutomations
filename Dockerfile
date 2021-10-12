FROM python:3.9 as base

WORKDIR /NotionAutomations
COPY ./ ./

RUN pip install -r requirements.txt

CMD bash