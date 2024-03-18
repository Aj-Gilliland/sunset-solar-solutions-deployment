
from django.contrib import admin
from django.urls import path
from app.views import home, contact, donate, career

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('Contact/', contact, name="contact"),
    path('Donate/', donate, name="donate"),
    path('Career/', career, name="career")
]
