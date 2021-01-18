from rest_framework import generics
from rest_framework.views import Response
from rest_framework import status
from .serializers import RegistrationSerializer
# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Account Created'}, status=status.HTTP_201_CREATED)
