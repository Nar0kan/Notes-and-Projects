from django.core.management.base import BaseCommand
from core.models import Journal, Category, Author
from random import randint
from datetime import date


categories = [
    'Sport',
    'Anime',
    'Cartoons',
    'Code',
    'Architecture',
    'Fantasy',
    'Music'
]


authors = [
    'William', 'John', 'Joe', 'Cally', 'Sandy', 'Mary', 'Den', 'Antonio', 'Lara'
]


def generate_author_name():
    return authors[randint(0, 8)]


def generate_category_name():
    return categories[randint(0, 6)]


def generate_view_count():
    return randint(0, 100)


def generate_is_reviewed():
    return False if randint(0, 1) == 0 else True


def generate_date():
    return date(year=randint(1980, 2020), month=randint(1, 12), day=randint(1, 28))


class Command(BaseCommand):
    
    def add_arguments(self, parser) -> None:
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the journal titles'
        )
    
    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt', 'r') as file:
            for row in file:
                title = row
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_date()
                views = generate_view_count()
                reviewed = generate_is_reviewed()

                author = Author.objects.get_or_create(name=author_name)

                journal = Journal(
                    title = title,
                    author = Author.objects.get(name=author_name),
                    publish_date = publish_date,
                    views = views,
                    reviewed = reviewed
                )
                journal.save()

                category = Category.objects.get_or_create(
                    name = category_name
                )

                journal.categories.add(Category.objects.get(name=category_name))
        
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
