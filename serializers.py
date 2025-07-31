from rest_framework import serializers
from .models import Students

class studentSerializers(serializers.ModelSerializer):
    class Meta :
        model=Students
        fields=[
            'id','stu_name','roll_no'
        ]