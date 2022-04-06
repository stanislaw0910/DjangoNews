from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="main.html")),
    path('users/', include('users.urls')),
    path('news/', include('news_and_comments.urls')),

]
