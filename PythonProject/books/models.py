from django.db import models

class BookType(models.TextChoices):
    STANDARD = 'standard'
    BADIIY = 'badiiy'
    ILMIY = 'ilmiy'


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField()

    def __str__(self):
        return f'{self.first_name}'
    class Meta:
        db_table = 'authors'
        ordering = ['-birth_date']
# Create your models here.
# id -> primary key-serial,
# title -> varchar(255),
# description -> text,
# author -> varchar(255),
# type -> varchar
class Books(models.Model):
    title  = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author,related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=BookType.choices, default=BookType.STANDARD)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'{self.title}'
    class Meta:
        db_table = 'books'
        ordering = ['-created_time']


"""
inser into authors (first_name, last_name, birth_date) values ("dadad","dadadad", "2024-2-1");

Select * from authors;

update auther set first_name = ?, last_name = ?, 

"""

"""
python manage.py shell


"""
