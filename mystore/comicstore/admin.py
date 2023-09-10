from django.contrib import admin
from .models import Author, Language, Book_series, Genre, Publisher, Product_details, Product


admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book_series)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Product_details)
admin.site.register(Product)


