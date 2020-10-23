from rest_framework import serializers

from .models import Label, CustomUser


class LabelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Label
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    labels = serializers.PrimaryKeyRelatedField(many=True, queryset=Label.objects.all(), required=False)
    extra_kwargs = {'password': {'write_only': True}}

    class Meta:
        model = CustomUser
        fields = ['email', 'labels', 'password']

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep.pop('password', None)  # this avoid returning password in views
        return rep

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
