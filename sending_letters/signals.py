import asyncio
import time

from django.dispatch import receiver

from django.dispatch import Signal
from . import models
from django.db.models import Q

user_signal = Signal()



@receiver(user_signal,
          dispatch_uid="status_task_send")  # Функция update_job_status_listeners будет вызвана только при сохранении экземпляра BordomaticPrivate
def status_task_send(sender, instance, **kwargs):
    '''
    Sends task status to the browser when a video was created
    '''
    campaign_instance = kwargs.get('inst')
    print(kwargs)
    # loop = asyncio.get_event_loop()
    # print(loop)
    print('**********сработал сигнал сохранения рассылки**************')
    clients = models.Client.objects.filter(
        Q(operator_code=campaign_instance.filter_mobile_operator_code) & Q(tag=campaign_instance.filter_tag)
    )

    for client in clients:
        models.Message.objects.create(
            campaign=campaign_instance, text=kwargs.get('text_message')
        )




# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db.models import Q
#
# from .models import Campaign
# from .tasks import *
#
#
#
# @receiver(post_save, sender=Campaign)
# def sending_letters(sender, instance, **kwargs):
#     print('**********сработал сигнал сохранения рассылки**************')