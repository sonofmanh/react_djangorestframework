from rest_framework import serializers
from contactVtwoapp.models import Contact


class Contactserializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'