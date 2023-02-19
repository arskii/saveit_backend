from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer


@api_view(['GET'])
def getRoutes(req):
    routes = [
        'api/auth/register',
        '/api/auth/login',
        '/api/auth/refresh-token'
    ]

    return Response(routes)

class GenerationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                'Message': 'User created successfully',
                'User': serializer.data}, status=status.HTTP_201_CREATED
            )
        
        return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
