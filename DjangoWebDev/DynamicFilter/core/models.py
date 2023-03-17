from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        FICTION = 'FIC'
        SCI_FI = 'SFI'
        FANTASY = 'FAN'
        MANGA = 'MAN'
        OTHER = 'OTH'
        HORROR = 'HOR'
        COMEDY = 'COM'
        DRAMA = 'DRA'
    
    title = models.CharField(max_length=128)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=3, choices = GenreChoices.choices)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title