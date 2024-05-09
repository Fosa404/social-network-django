from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [

    path('', views.feed, name='feed'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='form/login.html'), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('post/', views.create_posts, name='post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
