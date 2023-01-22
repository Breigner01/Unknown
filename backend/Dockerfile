FROM python:3.11.1-alpine3.17

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY .. .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]