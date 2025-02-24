from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book, Author, Publications, Article
from .serializer import BookSerializer, AuthorSerializer, PublicationsSerializer, ArticleSerializer


class PublicationsViews(APIView):
    def get(self, request, publication_id=None):
        if publication_id:
            publication = get_object_or_404(Publications, id=publication_id)
            serializer = PublicationsSerializer(publication)
            return Response(serializer.data)
        
        publications = Publications.objects.all()
        serializer = PublicationsSerializer(publications, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response({'message': 'Publication created successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)

    def put(self, request, publication_id):
        publication = get_object_or_404(Publications, id=publication_id)
        serializer = PublicationsSerializer(publication, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Publication updated successfully', "data": serializer.data})

    def delete(self, request, publication_id):
        publication = get_object_or_404(Publications, id=publication_id)
        publication.delete()
        return Response({'message': 'Publication deleted successfully'})        
            
            
            
class BookViews(APIView):
    def get(self, request, book_id=None):
        if book_id:  
            book = get_object_or_404(Book, id=book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
                
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book created successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)

    def put(self, request, book_id):  
        book = get_object_or_404(Book, id=book_id)  
        serializer = BookSerializer(book, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book updated successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)

    def delete(self, request, book_id):  
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully'})


class AuthorViews(APIView):
    def get(self, request, author_id=None):
        if author_id:  
            author = get_object_or_404(Author, id=author_id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Author created successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)

    def put(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Author updated successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)

    def delete(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        author.delete()
        return Response({'message': 'Author deleted successfully'})

    
class ArticleViews(APIView):
    def get(self, request, article_id=None):
        if article_id:
            article = get_object_or_404(Article, id=article_id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)            
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Article created successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Article updated successfully', "data": serializer.data})
        return Response({'error': serializer.errors}, status=400)
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)     
        article.delete()
        return Response({'message': 'Article deleted successfully'})

