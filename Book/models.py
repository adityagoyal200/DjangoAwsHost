from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
        
class Publications(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    published_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publications = models.ManyToManyField(Publications, related_name='articles')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    language = models.CharField(max_length=50)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books') 
    publications = models.ManyToManyField(Publications, related_name='books') 
    created_at = models.DateTimeField(auto_now_add=True)




