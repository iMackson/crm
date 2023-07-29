from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('<int:pk>/', views.lead_detail, name='detail'),
    path('<int:pk>/update/', views.lead_update, name='update'),
    path('create/', views.lead_create, name="create"),
    path('<int:pk>/delete/', views.lead_delete, name="delete")
]
