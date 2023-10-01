from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content' ,'body' , 'author' , 'isbn' , 'price']
    list_filter = ['title' , 'author' , 'isbn', 'price']
    search_fields = ['title' , 'content' , 'author' , 'isbn' , 'price']

