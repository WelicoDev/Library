from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content','body', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author' , None)
        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "The title of the book must consist of letters!",
                }
            )

        # check title and author from database existence
        if Book.objects.filter(title=title,author = author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "You cannot upload books with the same title and author!",
                }
            )

        return data

    def validate_price(self ,price):
        price = float(price)
        if price < 0 or price > 999999999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "The price was entered incorrectly, please check!",
                }
            )



# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=250)
#     content = serializers.CharField(max_length=255)
#     body = serializers.CharField()
#     author = serializers.CharField(max_length=250)
#     isbn = serializers.CharField(max_length=20)
#     price = serializers.DecimalField(max_digits=20 ,decimal_places=2)

