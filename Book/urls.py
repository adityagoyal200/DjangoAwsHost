from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.BookViews.as_view(),name='books'),
    path('books/',views.BookViews.as_view(),name='books'),
    path('books/<int:pk>/',views.BookViews.as_view(),name='book_detail'),
    path('authors/',views.AuthorViews.as_view(),name='authors'),
    path('authors/<int:author_id>/',views.AuthorViews.as_view(),name='author_detail'),
    path('publications/',views.PublicationsViews.as_view(),name='publications'),
    path('publications/<int:publication_id>/',views.PublicationsViews.as_view(),name='publication_detail'),
    path('articles/',views.ArticleViews.as_view(),name='articles'),
    path('articles/<int:article_id>/',views.ArticleViews.as_view(),name='article_detail'),
]

