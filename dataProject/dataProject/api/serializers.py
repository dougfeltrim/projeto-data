from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from dataProject.formulario import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class DividalSerializer(serializers.ModelSerializer):

#    nome = serializers.CharField(source='divida.name', read_only=True)
#    status = serializers.CharField(source='divida.status', read_only=True)

#    class Meta:
#        model = models.Dividas
#        fields = (nome, status, 'contents', )