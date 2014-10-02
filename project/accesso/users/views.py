from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class UserProfileView(DetailView):

    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user