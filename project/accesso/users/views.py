from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from .serializers import UserSerializer


class UserProfileView(DetailView):

    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    model = get_user_model()
    serializer_class = UserSerializer

    @list_route(methods=['get', ])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)