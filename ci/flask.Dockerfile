FROM tiangolo/uwsgi-nginx:python3.8

COPY ./ /app
COPY ./src/app/uwsgi.ini /app

RUN python -m pip install --upgrade pip

COPY ./src/app/requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt