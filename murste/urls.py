from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
import notifications.urls
from users.views import FollowUser, ViewFollowers

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #re_path(r'^reviews/', include('reviews.urls')),
    #re_path(r"^ratings/", include("pinax.ratings.urls", namespace="pinax_ratings")),
    path('messages/', include('directmessages.urls')),
    path('memberships/', include('memberships.urls')),
    path('projects/', include('core.urls')),
    path('', include('murstebase.urls')),
    path('jobs/', include('jobs.urls')),
    #path('comments/', include('comments.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('user/<str:username>/follow/', FollowUser.as_view(), name='user_follow'),
    path('user/<str:username>/followers/', ViewFollowers.as_view(), name='user_followers'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="core/robots.txt", content_type="text/plain"),
    ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
