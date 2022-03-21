from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from chat.models import LostPetBoard, LostPetBoardImage
from chat.serializers import LostPetBoardSerializer, LostPetBoardCreateSerializer, LostPetBoardImageSerializer


class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoard.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardSerializer
        return LostPetBoardCreateSerializer


class LostPetImageViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoardImage.objects.all()
    serializer_class = LostPetBoardImageSerializer
