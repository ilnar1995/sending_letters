FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies

WORKDIR /usr/src/django_project

COPY req.txt /usr/src/req.txt
RUN apt-get update \
    && apt-get install -yyq ncat
RUN pip install -r /usr/src/req.txt

COPY .. /usr/src/django_project

#CMD ["python", "base.py"]
COPY /docker/entrypoint.sh .
COPY /docker/entrypoint-celery.sh .
#RUN chmod +x ./entrypoint.sh
#RUN chmod +x ./entrypoint-celery.sh

EXPOSE 8000
EXPOSE 5555
# ENTRYPOINT ["/usr/src/django_project/entrypoint.sh"]
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
