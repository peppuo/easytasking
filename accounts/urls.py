from django.urls import include, path, reverse_lazy
from accounts.views import logout, login, registration, user_profile
# from accounts import url_reset


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
    path('profile/', user_profile, name='profile'),
# path('password-reset/', include(url_reset)),
]
