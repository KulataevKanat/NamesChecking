from rest_framework import serializers

from .models import NamesWoman, NamesMan


class NamesWomanSerializer(serializers.ModelSerializer):
    """Сериализатор имён женщин"""

    class Meta:
        model = NamesWoman
        fields = '__all__'


class NamesManSerializer(serializers.ModelSerializer):
    """Сериализатор имён мужчин"""

    class Meta:
        model = NamesMan
        fields = '__all__'


class ContactSerializer(serializers.Serializer):
    """Сериализатор контактов Bitrix24"""

    id = serializers.IntegerField()
    name = serializers.CharField()
    gender = serializers.CharField()
