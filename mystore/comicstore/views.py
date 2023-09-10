from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from comicstore.models import Product, Author, Book_series, Genre, Language, Product_details
from comicstore.serializer import ProductSerializer, AuthorSerializer, BookSeriesSerializer, GenreSerializer, LanguageSerializer, ProdDetailsSerializer


class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'product': serializer.data})


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