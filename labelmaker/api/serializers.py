from rest_framework import serializers

from .models import Label, CustomUser


class LabelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Label
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    labels = serializers.PrimaryKeyRelatedField(many=True, queryset=Label.objects.all())

    class Meta:
        model = CustomUser
        fields = ['email', 'labels']
