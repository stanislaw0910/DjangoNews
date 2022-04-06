from django.urls import path
from .views import NewsCreateView, IndexNews, NewsDetailView, NewsUpdateView, News_tags


urlpatterns = [
    path('',  IndexNews.as_view(), name='news'),
    #path('', News_tags, name='news'),
    path('create', NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>', NewsDetailView.as_view()),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
]