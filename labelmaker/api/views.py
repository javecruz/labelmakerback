from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsLabelOwner
from .models import Label, CustomUser
from .serializers import LabelSerializer, UserSerializer


class LabelView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['retrieve', "list"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsLabelOwner]
        return [permission() for permission in permission_classes]

    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
