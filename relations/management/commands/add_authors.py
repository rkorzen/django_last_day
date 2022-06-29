# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html


from django.core.management.base import BaseCommand
from relations.utils import generate_authors

class Command(BaseCommand):
    help = 'Generate 10 authors'

    def handle(self, *args, **kwargs):
        n = kwargs.get("total", 10)
        generate_authors(n)
        print("Finished..")

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of authors to be created')
