from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from menu import Menu, MenuItem

def user_is_staff(request):
    return request.user.is_staff

for item in (
        MenuItem(_("E-mail Addresses"),
                 reverse("account_email"),
                 weight=10,
                 icon="envelope"),
        MenuItem(_("Account Connections"),
                 reverse("socialaccount_connections"),
                 weight=10,
                 icon="globe"),
        MenuItem(_("Change Password"),
                 reverse("account_change_password"),
                 weight=10,
                 icon="key"),
        MenuItem("Applications",
                 reverse("oauth2_provider:list"),
                 weight=80,
                 separator=True,
                 icon='cubes',
                 check=user_is_staff),
        MenuItem("Admin",
                 reverse("admin:index"),
                 weight=80,
                 icon='gears',
                 check=user_is_staff),
        MenuItem("Logout",
                 reverse("account_logout"),
                 weight=90,
                 separator=True,
                 icon="sign-out"),
):
    Menu.add_item("user_menu", item)