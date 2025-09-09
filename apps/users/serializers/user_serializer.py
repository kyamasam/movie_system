from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    
    class Meta:
        model = User
        fields = ["id", "first_name","password", "username","last_name", "middle_name", "phone_code", "phone"]
        write_only_fields =["password"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    
    
    class Meta:
        model = User
        fields = ["id", "first_name","password", "token","refresh","username","last_name", "middle_name", "phone_code", "phone"]
        write_only_fields =["password"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user