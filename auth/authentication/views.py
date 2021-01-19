from rest_framework import generics
from rest_framework.views import Response
from rest_framework import status
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class RegisterView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(email=user['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        abs_url = 'http://' + current_site + relative_link + "?token=" + str(token)

        body = 'Hi ' + user.username + ', \n' + 'Use below link to verify your account. \n' + abs_url

        data = {'email_body': body, 'email_subject': 'Verify your account', 'email_to': user.email}
        
        
        Utils.send_mail(data)

        return Response({'message': 'Account Created'}, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    
    def get(self, request):
        pass


class LoginView(generics.CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        return Response({}, status=status.HTTP_200_OK)
