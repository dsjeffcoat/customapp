from django.urls import path
from homepage import views as v

urlpatterns = [
    path('', v.index, name='homepage'),
    path('login/', v.login_view, name="login_view"),
    path('signup/', v.signup_view, name="signup_view"),
    path('logout/', v.logout_view, name="logout_view"),
]
