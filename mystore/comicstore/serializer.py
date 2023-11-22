from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField, SlugRelatedField
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from comicstore.models import Product, Author, Book_series, Genre, Language, Product_details
# from comicstore.models import Product_details    


class ProdDetailsSerializer(ModelSerializer):

    class Meta:
        model = Product_details
        fields = ['pages', 'height', 'width', 'weight', 'publish_date',
                  'circulation','age_restrictions','isbn'] 

class ProductSerializer(WritableNestedModelSerializer): #для вложенных полей. Другой вариант, насколько я понимаю, это прописать метод create вручную в сериализаторе   
    author = StringRelatedField(read_only=True) #для того, чтобы отражался не id, а имя из связанной таблицы. Так же необходимо прописать магический метод __str__ в моделях
    publisher = StringRelatedField(read_only=True)
    book_series = StringRelatedField(read_only=True)
    genre = StringRelatedField(read_only=True)
    language = StringRelatedField(read_only=True)
    prod_details = ProdDetailsSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Чтобы поле пользователь автоматически заполнялось именем_пользователя, который внес измененения (до добавления этой строчки поле пользователь не заполняется и присутствует выбор определенного пользователя, что не явл. правильным). Также теперь поле пользователь будет скрыто
    #-----------------------------------------------------------------
    # если поле прописано сверху, например language = Str...() и снизу 
    # прописано вручную, то в поле для ввода drf в браузере, 
    # language не будет отражаться, то есть для того, чтобы они отражались надо 
    # не прописывать сверху (но тогда будет выводиться только id, 
    # вместо строки). Это мои наблюдения, почему так пока не до конца понимаю
    # update: я разобрался, потому что поля с типом 
    # StringRelatedField не поддерживают операции записи, 
    # поэтому для них всегда должен быть указан параметр read_only=True.
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'description','price', 'cover_type', 'author', 
                  'publisher', 'book_series', 'genre', 'language', 'prod_details', 'user'] #'__all__'
    
    # def to_representation(self, instance):
    #     data =  super(ProductSerializer,self).to_representation(instance)
    #     data['author'] = instance.author.author_name
    #     return data
    # def create(self, validated_data):
    #     pr_details = validated_data.pop('prod_details')
    #     details = Product.objects.create(**validated_data)
    #     # for pr_detail in pr_details:
    #     Product_details.objects.create(details=details, **pr_details)
    #     return details

class AuthorSerializer(ModelSerializer): #не думаю, что пока мне нужны эти второстепенные сериализаторы
    # authors = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Author
        fields = ['authors'] 


class BookSeriesSerializer(ModelSerializer):
    # series = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Book_series
        fields = ['series']


class GenreSerializer(ModelSerializer):
    # genres = StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Genre
        fields = ['genres']


class LanguageSerializer(ModelSerializer):
    # languages = StringRelatedField(many = True, read_only = True)
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

    def create(self, validated_data): # если убрать всю эту фуекцию create, то пароль не будет хэшироваться в бд
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
