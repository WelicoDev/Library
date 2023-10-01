from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics , status

# Create your views here.
# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApi(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books , many=True).data
        data = {
            "status":f"Returned {len(books)} books",
            "books":serializer_data,
        }

        return Response(data)

# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApi(APIView):
    def get(self ,request , pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status": "Successfully",
                "book": serializer_data,
            }
            return Response(data ,status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                },
                status=status.HTTP_400_BAD_REQUEST
                )



# class BookUpdateApi(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApi(APIView):
    def put(self , request , pk):
        try:
            book = Book.objects.get(pk=pk)
            data = request.data
            serializer = BookSerializer(instance=book , data=data ,partial=True)
            if serializer.is_valid(raise_exception=True):
                book_saved = serializer.save()

                return Response(
                    {
                        "status": True,
                        "message":f"Book {book_saved} updated successfully"
                    }, status=status.HTTP_200_OK
                    )
        except Exception:
            return Response(
                {
                    "status": False,
                    "message": "Book is not found"
                }, status=status.HTTP_400_BAD_REQUEST
            )

# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApi(APIView):
    def delete(self , request , pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(
                {
                    "status":True,
                    "message":"Successfully deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                } , status=status.HTTP_400_BAD_REQUEST
            )

# class BooksCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BooksCreateApi(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            books = serializer.save()
            data = {
                'status':f"Books are saved to the database",
                'books':data,
            }
            return Response(data)
        else:
            return Response(
                data = {
                    "status":False,
                    "message":"Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )

class BooksListCreateApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# function books list api
"""@api_view(['GET'])
def books_list_api(request , *args , **kwargs):
    books = Book.objects.all()
    serializers = BookSerializer(books , many=True)
    return Response(serializers.data)"""