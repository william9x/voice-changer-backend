FROM python:3.10.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update -y && \
      apt-get upgrade -y && \
      apt-get install -y build-essential

RUN python -m venv .venv && \
        source .venv/bin/activate && \
        pip install pyworld && \
        pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]