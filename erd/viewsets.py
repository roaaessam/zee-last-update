from django.contrib.auth.models import User
from .Serializers import UserSerializer
from rest_framework import viewsets
from .models import Profile
from .permissions import IsUserOwnerOrGetAndPostOnly
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Register, Profile
from .Serializers import RegisterSerializers

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsUserOwnerOrGetAndPostOnly]
    queryset=User.objects.all()
    serializer_class=UserSerializer



    # views.py


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Create a User instance
            user = User.objects.create_user(
                username=serializer.validated_data['name'],
                email=serializer.validated_data['emaill'],
                password=serializer.validated_data['Password']
            )

            # Create a Profile instance linked to the User
            profile = Profile.objects.create(
                user=user
                # You can handle 'image' field from serializer if needed
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

