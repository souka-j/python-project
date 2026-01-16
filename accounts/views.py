from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()       # Tous les utilisateurs
    serializer_class = UserSerializer   # Sérializer pour transformer en JSON
