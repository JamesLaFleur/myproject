from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from rest_framework.decorators import api_view

from rest_framework import status

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView


from comicstore.models import Product, Author, Book_series, Genre, Language, Product_details
from comicstore.serializer import *



class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookSeriesViewSet(ModelViewSet):
    queryset = Book_series.objects.all()
    serializer_class = BookSeriesSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class LangugeViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ProdDetailsViewSet(ModelViewSet):
    queryset = Product_details.objects.all()
    serializer_class = ProdDetailsSerializer



class UserCreateViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    def create_user(request):
        serializer = UserCreateSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


    
class MyTokenObtainPairView(TokenObtainPairView): 
    serializer_class = MyTokenObtainPairSerializer


class UserInfoViewSet(ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()
    def user_info(request, pk):
        user = User.objects.get(id=pk)
        user_info = User.objects.filter(User=user)
        if request.user.is_authenticated:
            return user_info
        else:
            return Response(
                {'data': 'These is not your data'}
            )
   