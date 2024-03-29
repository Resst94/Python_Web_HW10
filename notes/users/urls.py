from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import LoginForm
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/signin.html', authentication_form=LoginForm,
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
