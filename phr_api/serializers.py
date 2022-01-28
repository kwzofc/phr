from rest_framework import serializers
from phr.models import PHR
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password',)



class PHRSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PHR