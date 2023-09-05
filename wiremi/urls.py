from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Wiremi APIs",
        default_version='v1',
        description="it contains the apis for a financial transaction systems for leasing and joint venture capitalism",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls')),
    # path('api/v1/projects/', include('projects.urls')),
    # path('api/v1/savings/', include('savings.urls')),
    # path('api/v1/wallet/',include('wallets.urls')),
    # path('api/v1/investment/',include('investment.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]