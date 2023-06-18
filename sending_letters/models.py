from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.core.validators import RegexValidator


class Client(models.Model):
    phone_number_validator = RegexValidator(
        regex=r"^7\d{10}$",
        message="Номер телефона клиента в формате 7XXXXXXXXXX (X-цифра от 0 до 9)",)
    tag = models.CharField(_('Tag'), max_length=50, validators=[MinLengthValidator(1)])
    operator_code = models.CharField(_("Operator code"), max_length=3, validators=[MinLengthValidator(3)], editable=False)
    phone_number = models.CharField(
        _("Phone number"),
        validators=[phone_number_validator],
        unique=True,
        max_length=11)

    def __str__(self):
        return f"Client {self.id} with number {self.phone_number}"

    def save(self, *args, **kwargs):
        self.operator_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)

    class Meta:
        db_table = "app_sending_letters_client"
        ordering = ["id"]


class Message(models.Model):
    text = models.CharField(_('Tag'), max_length=500, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return self.text

    class Meta:
        db_table = "app_sending_letters_message"
        ordering = ["id"]


class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    filter_mobile_operator_code = models.CharField(
        verbose_name="Search by mobile operator code", max_length=3, blank=True,
        validators=[MinLengthValidator(1)]
    )
    filter_tag = models.CharField(_("Tag"), max_length=50, blank=True)

    def __str__(self):
        return f"Campaign {self.id} with start time {self.start_time}"

    class Meta:
        db_table = "app_sending_letters_campaign"
        ordering = ["id"]


