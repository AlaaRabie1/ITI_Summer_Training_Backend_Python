from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailAPIView(APIView):

    def get_book(self, pk):
        try:
            return Book.objects.get(pk=pk)
        
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk):
        book = self.get_book(pk)
        
        if book == None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_book(pk)
        
        if not book:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_book(pk)
        
        if book == None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response({'message': 'Book deleted'}, status=status.HTTP_204_NO_CONTENT)
