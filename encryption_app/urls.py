from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('channel/create/', views.ChannelCreateView.as_view(), name='channel_create'),
    path('channel/join/', views.channel_join, name='channel_join'),
    path('channel/<int:channel_id>/encrypt/', views.encrypt_message, name='encrypt'),
    path('channel/<int:channel_id>/decrypt/', views.decrypt_message, name='decrypt'),
    path('channel/<int:channel_id>/messages/', views.channel_messages, name='channel_messages'),
    path('help/', views.HelpView.as_view(), name='help'),
    # Add login/logout if using Django auth views
]