FROM python:3.6

WORKDIR "/opt/magazine"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY="dw-m=d3!i=qkf77f0z37#ejzhuplq!ccu96wd5*380-*t5)7pf"
ENV DJANGO_SETTINGS_MODULE="magazine.settings"
RUN python3 manage.py migrate

ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000