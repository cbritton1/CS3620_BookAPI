from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer


class ClassicsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='classics')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='historical_fiction')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='science_fiction')
    serializer_class = BookSerializer


class ShortStoriesViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='short_stories')
    serializer_class = BookSerializer


class SuspenseViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='suspense')
    serializer_class = BookSerializer


class CookbooksViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='cookbooks')
    serializer_class = BookSerializer
