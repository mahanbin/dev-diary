"""devDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import diaryboard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diaryboard.views.index, name='index'),
    path('boardview/', diaryboard.views.boardview, name='boardview'),
    path('new/', diaryboard.views.boardwrite, name='boardwrite'),
    path('board/<int:post_id>/', diaryboard.views.detail, name='detail'),
    path('board/<int:post_id>/update/', diaryboard.views.update, name='update'),
    path('board/<int:post_id>/delete/', diaryboard.views.delete, name='delete'),
]
