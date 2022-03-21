from rest_framework import serializers
from chat.models import LostPetBoard, LostPetBoardImage


class LostPetBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardImage
        fields = "__all__"


class LostPetBoardCreateSerializer(serializers.ModelSerializer):
    board_image = LostPetBoardImageSerializer

    class Meta:
        model = LostPetBoard
        fields = ["board_image", "title", "content"]


class LostPetBoardSerializer(serializers.ModelSerializer):
    lost_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    board_image = LostPetBoardImageSerializer(many=True, read_only=True)

    class Meta:
        model = LostPetBoard
        fields = ["title", "content", "board_image",
                  "lost_time", "created_at", "updated_at"]