from .models import CustomUser, UserProfile
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30,write_only=True)
    password_confirm = serializers.CharField(max_length=30,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','mobile_number','username','password','password_confirm']

    def validate(self,data):
        email = data.get('email')
        mobile_number = data.get("mobile_number")

        if not email and not mobile_number:
            raise serializers.ValidationError("Either mobile number or email is required.")
        
        if email and CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already linked with another account.")
        
        if mobile_number and CustomUser.objects.filter(mobile_number=mobile_number).exists():
            raise serializers.ValidationError("This mobile number is already linked with another account.")
        
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError("Passwords doesn't match.")

        return super().validate(data)
    
    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return CustomUser.objects.create_user(**validated_data)



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


    