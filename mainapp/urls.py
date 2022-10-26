from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('post/<int:pk>/', ShowPost.as_view(), name='post'),    
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)