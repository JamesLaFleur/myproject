from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField, SlugRelatedField
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from comicstore.models import Product, Author, Book_series, Genre, Language, Product_details  


class ProdDetailsSerializer(ModelSerializer):

    class Meta:
        model = Product_details
        fields = ['pages', 'height', 'width', 'weight', 'publish_date',
                  'circulation','age_restrictions','isbn'] 

class ProductSerializer(WritableNestedModelSerializer): 
    author = StringRelatedField(read_only=True)
    book_series = StringRelatedField(read_only=True)
    genre = StringRelatedField(read_only=True)
    language = StringRelatedField(read_only=True)
    prod_details = ProdDetailsSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'description','price', 'cover_type', 'author', 
                  'publisher', 'book_series', 'genre', 'language', 'prod_details', 'user'] #'__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['authors'] 


class BookSeriesSerializer(ModelSerializer):
    class Meta:
        model = Book_series
        fields = ['series']


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genres']


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = ['languages']



class UserCreateSerializer(ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('username', 'password', 'email','token')
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token


    class Meta:
        model = User
        fields = '__all__'




class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email'] 
