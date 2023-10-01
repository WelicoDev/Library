from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApi , BookDetailApi , BookUpdateApi ,BookDeleteApi , BooksCreateApi ,\
                    BooksListCreateApi , BookEditApi ,BookViewSet

router = SimpleRouter()
router.register('books' , BookViewSet , basename='books')
urlpatterns = [
    path('books/' , BookListApi.as_view() , name = 'books_list'),
    path('books/<int:pk>/' , BookDetailApi.as_view() , name ='books_detail'),
    # path('bookslist/' , books_list_api , name ='books_api'),
    path('books/<int:pk>/update/' , BookUpdateApi.as_view() , name ='books_edit'),
    path('books/<int:pk>/delete/' , BookDeleteApi.as_view() , name ='books_delete'),
    path('books/create/' , BooksCreateApi.as_view() , name ='books_create'),
    path('books-list/create/' , BooksListCreateApi.as_view() , name = 'bookslist_create'),
    path('books/<int:pk>/edit/' , BookEditApi.as_view() , name='books_edit'),
]
# urlpatterns += router.urls