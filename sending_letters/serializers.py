from rest_framework import serializers
from . import models
from . import signals


class MessageSerializer(serializers.ModelSerializer):
    campaign = serializers.CharField(
        source='campaign.id', read_only=True, allow_null=True)

    class Meta:
        model = models.Message
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    text_message = serializers.CharField(write_only=True)

    class Meta:
        model = models.Campaign
        fields = "__all__"

    def create(self, validated_data):
        del validated_data['text_message']
        return super().create(validated_data)

    def save(self, **kwargs):
        print(self.context.get("request").data.get("text_message"))
        instance = super().save(**kwargs)
        signals.user_signal.send(sender=None, instance=None, text_message=self.context.get("request").data.get("text_message"), inst=instance)
        return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"
