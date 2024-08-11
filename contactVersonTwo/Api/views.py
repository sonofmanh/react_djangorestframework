from rest_framework.response import Response
from rest_framework.decorators import api_view
from contactVtwoapp.models import Contact
from .  serializers import Contactserializers

@api_view(['GET'])
def gretData(request):
    contacts = Contact.objects.all()
    serializer = Contactserializers(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializers = Contactserializers(data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)