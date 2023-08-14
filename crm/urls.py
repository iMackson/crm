
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from leads.views import landing_page, LandingPageView, SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
