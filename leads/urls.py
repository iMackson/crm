from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', views.lead_update, name='lead-update'),
    path('create/', views.LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/delete/', views.lead_delete, name="lead-delete")
]
