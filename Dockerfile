FROM python:3.10.12

ENV PYTHONUNBUFFERED=1

WORKDIR /menu

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]