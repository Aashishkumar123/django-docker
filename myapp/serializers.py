from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import student

class studentserializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = ['id','name','email']