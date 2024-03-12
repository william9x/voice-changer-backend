FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

RUN apt-get update -y && \
      apt-get upgrade -y && \
      apt-get install -y build-essential make nano

COPY ../requirements.txt /app/requirements.txt

RUN pip install pyworld
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY .. /app/

CMD ["python", "main.py"]