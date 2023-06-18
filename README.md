# Сервис управления рассылками

##  Запуск
### команда на линукс:
    sudo docker compose up 
### команда на windows:
    docker-compose up

(!!!! перед запуском на windows необходимо в папке docker у файлов entrypoint.sh и
entrypoint-celery.sh поменять кодировки окончания строк с CRLF на LF)

клиенты загруюаются из csv файла автоматический при первом запуске приложения

### Cтраница сваггера:
[http://localhost:8000/swagger](http://localhost:8000/swagger)
### Cтраница flower для просмотра очереди задач:
[http://localhost:5555/](http://localhost:5555)






