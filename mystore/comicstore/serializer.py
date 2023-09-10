from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField, SlugRelatedField

from comicstore.models import Product, Author, Book_series, Genre, Language, Product_details
from comicstore.models import Product_details    


class ProdDetailsSerializer(ModelSerializer):
    class Meta:
        model = Product_details
        fields = ['pages', 'height', 'width', 'weight', 'publish_date',
                  'circulation','age_restrictions','isbn'] 

class ProductSerializer(ModelSerializer):
    # author = StringRelatedField(read_only = True)
    # book_series = StringRelatedField(read_only = True)
    # genre = StringRelatedField(read_only = True)
    # language = StringRelatedField(read_only = True)
    prod_details = ProdDetailsSerializer()
    class Meta:
        model = Product
        fields = ['name', 'description','price', 'cover_type', 'author', 
                  'publisher', 'book_series', 'genre', 'language', 'prod_details'] #'__all__'
    
    def create(self, validated_data):
        pr_details = validated_data.pop('prod_details')
        details = Product.objects.create(**validated_data)
        # for pr_detail in pr_details:
        Product_details.objects.create(details=details, **pr_details)
        return details

class AuthorSerializer(ModelSerializer):
    authors = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Author
        fields = ['authors'] 


class BookSeriesSerializer(ModelSerializer):
    series = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Book_series
        fields = ['series']


class GenreSerializer(ModelSerializer):
    genres = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Genre
        fields = ['genres']


class LanguageSerializer(ModelSerializer):
    languages = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Language
        fields = ['languages']

