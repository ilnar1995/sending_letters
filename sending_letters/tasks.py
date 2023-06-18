from django_project.celery import app
from .models import Mailing, Message

@app.task(bind=True, retry_backoff=True)
def send_messages(self, mailing_instance_dict, message_text, client_id):
    """
    sending and creating messages for each client
    """
    mailing_inst = Mailing.objects.get(id=mailing_instance_dict.get("id"))
    Message.objects.create(mailing=mailing_inst, text=message_text)

    print(
        f'сообщение: "{message_text}", отправлено клиенту с id:{client_id} в рассылке с id:{mailing_instance_dict.get("id")}'
    )
