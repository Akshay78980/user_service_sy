from django.shortcuts import render
from .serializers import CustomUserSerializer, UserProfileSerializer
from .models import CustomUser, UserProfile

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

# Create your views here.


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return super().get_queryset().filter(id=self.request.user.id)
        return super().get_queryset()


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow users to see their profile
        return super().get_queryset().filter(user=self.request.user)



class UserRegistrationAPI(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        