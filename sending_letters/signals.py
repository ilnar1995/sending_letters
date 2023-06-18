from django.dispatch import receiver
from django.dispatch import Signal
from . import models
from django.utils import timezone
from .tasks import send_messages

user_signal = Signal()


@receiver(user_signal,
          dispatch_uid="signal_for_sending_messages")
def signal_for_sending_messages(sender, instance, **kwargs):
    """
    Signal for sending messages
    """
    print('**********сработал сигнал для рассылки**************')
    mailing_instance = kwargs.get('mailing_inst')
    mailing_instance_dict = kwargs.get('mailing_inst').__dict__
    del mailing_instance_dict['_state']
    message_text = kwargs.get('text_message')

    clients = models.Client.objects.all()
    if mailing_instance_dict.get('filter_mobile_operator_code'):
        clients = clients.filter(operator_code=mailing_instance_dict.get('filter_mobile_operator_code'))
    if mailing_instance_dict.get('filter_tag'):
        clients = clients.filter(tag=mailing_instance_dict.get('filter_tag'))

    for client in clients:
        if timezone.now() <= mailing_instance.end_time:
            if mailing_instance.start_time <= timezone.now():
                send_messages.apply_async(
                    (mailing_instance_dict, message_text, client.id),
                    eta=mailing_instance.start_time,
                    expires=mailing_instance.end_time,
                )
            else:
                send_messages.apply_async(
                    (mailing_instance_dict, message_text, client.id),
                    expires=mailing_instance.end_time,
                )
