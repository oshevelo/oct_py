from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    login = serializers.CharField()
    email = serializers.EmailField()
    passwd = serializers.CharField()
    passwd1 = serializers.CharField()

    class Meta:
        fields = ('passwd', 'passwd1', 'login', 'email')


    def validate_login(self, value):
        if User.objects.filter(username=value).count()>0:
            raise serializers.ValidationError('bad login')
        return value

    def validate_passwd(self, value):
        raise  serializers.ValidationError('bad passwd ')
        return value

    def validate(self, data):
        raise serializers.ValidationError('bad passwd ')
        if data['passwd'] != data['passwd1']:
            raise serializers.ValidationError('bad passwd ')
        return data
        
    def create(self, data):
        print('create')
        return data

