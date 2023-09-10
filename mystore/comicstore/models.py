from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.author_name  # f'{self.author_name}'


class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.language

class Book_series(models.Model):
    book_series_name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.book_series_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.genre_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=40)


class Product_details(models.Model):
    pages = models.IntegerField()
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()
    publish_date = models.DateField()
    circulation = models.IntegerField('Тираж')
    age_restrictions = models.IntegerField()
    isbn = models.IntegerField()
    # def __init__(self, id, pages, height, width, weight, publish_date, circulation, age_restrictions, isbn):
    #     self.pages = pages
    #     self.id = id
    #     self.height = height
    #     self.width = width
    #     self.weight = weight
    #     self.publish_date = publish_date
    #     self.circulation = circulation
    #     self.age_restrictions = age_restrictions
    #     self.isbn = isbn
        #f'{self.pages}{self.height}{self.width}{self.weight}{self.publish_date}{self.circulation}{self.age_restrictions}{self.isbn}'



class Product(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, related_name='publishers', on_delete=models.CASCADE)
    book_series = models.ForeignKey(Book_series,related_name='series', on_delete=models.CASCADE)
    cover_type = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, related_name='genres', on_delete=models.CASCADE)
    prod_details = models.OneToOneField(Product_details, related_name='details', on_delete=models.CASCADE)
    language = models.ForeignKey(Language,related_name='languages', on_delete=models.CASCADE)

   





