from rest_framework import serializers


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')

class UserRegisterSerializer(serializers.Serializer):
    username= serializers.CharField(required= True)
    email= serializers.EmailField(required= True, validators= [clean_email])
    password = serializers.CharField(required= True, write_only= True)
    password2 = serializers.CharField(required= True, write_only= True)

    #Field Level
    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError('user name cant be admin')
        return value

    #Object Level  # Overwrite Validate method
    def validate(self, data):
        if data['password'] != data['password2'] :
            raise serializers.ValidationError('passwords must match')
        return data
