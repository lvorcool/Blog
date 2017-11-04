from django import forms
from django.core.exceptions import ValidationError
from rest_framework import serializers
from studyone.models import users

class UserSerializer(serializers.ModelSerializer):

    def words_validator(usersname):

        if  len(usersname) < 1:
            raise ValidationError({'status':10021, 'message':'字段不能为空'})

    def words_validator(password):
        if  len(password) < 1:
            raise ValidationError({'status':10021, 'message':'字段不能为空'})

    def words_validator(name):
        if  len(name) < 1:
            raise ValidationError({'status':10021, 'message':'字段不能为空'})

    class Meta:
        model = users
        fields = '__all__'


