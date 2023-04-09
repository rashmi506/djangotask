from rest_framework import serializers
from rest_framework import clientss

class clientssSerializer(Serializers.ModelSerializer):
    class Meta:

        model=clientss
       # fields=('client_name','lastname')
        fields='__all__'