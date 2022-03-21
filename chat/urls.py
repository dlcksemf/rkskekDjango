from django.urls import include, path
from rest_framework.routers import DefaultRouter
from chat.views import LostPetViewSet, LostPetImageViewSet

app_name = "lost_pet_board"

router = DefaultRouter()
router.register("posts", LostPetViewSet)
router.register("image", LostPetImageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]