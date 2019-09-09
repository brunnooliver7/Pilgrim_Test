from rest_framework.viewsets import ModelViewSet
from contributors.models import Contributor
from .serializers import ContributorSerializer
from rest_framework.filters import SearchFilter
from books.models import Book
from rest_framework.response import Response
from rest_framework.decorators import action

class ContributorViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    filter_backends = (SearchFilter,)
    search_fields = (
        'id', 'name', 'author', 'editor', 'reviewer',
        'email', 'country')
