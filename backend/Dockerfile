FROM python:3.8.10

COPY . /app/backend


WORKDIR /app/backend

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]