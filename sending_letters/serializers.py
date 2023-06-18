from rest_framework import serializers
from . import models
from . import signals


class MessageSerializer(serializers.ModelSerializer):
    mailing_id = serializers.IntegerField(
        source='mailing.id', read_only=True, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True, allow_null=True)

    class Meta:
        model = models.Message
        fields = ('id', 'mailing_id', 'created_at', 'text',)


class MailingSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    text_message = serializers.CharField(max_length=500, write_only=True)
    filter_mobile_operator_code = serializers.CharField(max_length=3, required=True)
    filter_tag = serializers.CharField(max_length=50, required=False)
    class Meta:
        model = models.Mailing
        fields = "__all__"

    def create(self, validated_data):
        del validated_data['text_message']
        return super().create(validated_data)

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        signals.user_signal.send(sender=None, instance=None,
                                 text_message=self.context.get("request").data.get("text_message"), mailing_inst=instance)
        return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"
