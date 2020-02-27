from django.urls import path,include
from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import url
from authentication import views
from django.views.generic.base import TemplateView

login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), 'home')

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home' ),

    ]


# kwargs={'redirect_authenticated_user': True})