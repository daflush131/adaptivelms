from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls', )),
    path('remotelab/', include('remotelab.urls')),
    path('lessons/', include('learncontent.urls')),


    path('', CustomLoginView.as_view(), name='root_redirect'),
]
