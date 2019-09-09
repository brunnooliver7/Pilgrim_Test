from rest_framework.viewsets import ModelViewSet
from books.models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter

class BookViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
