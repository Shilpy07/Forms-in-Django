from rest_framework import serializers
from modelform import models


class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentRecord
        fields = ('id', 'name', 'enrollment', 'faculty', 'year')

class CustomerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerRecord
        fields = ('id', 'name', 'customer_id')
