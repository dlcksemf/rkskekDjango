from typing import Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as OriginTokenObtainPairSerializer, \
                                                 TokenRefreshSerializer as OriginTokenRefreshSerializer

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["user_num", "username", "password", "password2", "nickname", "birthdate"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return attrs

    def create(self, validated_data):
        nickname = validated_data["nickname"]
        username = validated_data["username"]
        password = validated_data["password"]
        birthdate = validated_data.get("birthdate", None)

        new_user = User(nickname = nickname, username=username, birthdate=birthdate)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["user_num"] = self.user.user_num
        data["is_staff"] = self.user.is_staff
        data["username"] = self.user.username
        data["nickname"] = self.user.nickname

        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass