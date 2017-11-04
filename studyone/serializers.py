from django.contrib.auth.models import User, Group
from rest_framework import serializers
from studyone.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from studyone import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        field = ('url', 'usersname', 'email', 'groups' )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ('url', 'name')

"""
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # required=False : 非必填项目
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineons = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

"""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        field = ('id', 'title', 'code', 'lineons', 'language', 'style', 'created')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
