from rest_framework import serializers
from .models import Book,Author,Publications,Article

        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),write_only=True)
    publications = serializers.PrimaryKeyRelatedField(queryset=Publications.objects.all(),many=True,write_only=True)
    
    publications_data = PublicationsSerializer(source='publications',many=True, read_only=True)
    author_data = AuthorSerializer(source='author',read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):  
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),write_only=True)
    publications = serializers.PrimaryKeyRelatedField(queryset=Publications.objects.all(),many=True,write_only=True)
    
    publications_data = PublicationsSerializer(source='publications',many=True, read_only=True)
    author_data = AuthorSerializer(source='author',read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        


