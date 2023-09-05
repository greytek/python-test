from django.urls import path

from users.views import user_registration, user_login, logout_view, change_password

urlpatterns = [
    path('register/', user_registration),
    path('login/', user_login),
    # path('me/', UserView),
    path('logout/', logout_view),
    path('change-password/', change_password)
]
