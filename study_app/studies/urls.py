from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_study, name='add_study'),
    path('view/<int:pk>/', views.view_study, name='view_study'),
    path('edit/<int:pk>/', views.edit_study, name='edit_study'),
    path('delete/<int:pk>/', views.delete_study, name='delete_study'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
