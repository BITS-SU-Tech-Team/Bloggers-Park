from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.bloglist, name='blog-home'),
    path('<slug:slug>/', views.blog, name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
