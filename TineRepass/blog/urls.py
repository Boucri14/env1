from django.urls import path
from .views import index, signup, article

urlpatterns = {
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article-01"),
    path('compte/nouveau/', signup, name="signup")

}
