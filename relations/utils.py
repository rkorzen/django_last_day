from typing import List

from faker import Faker

from relations.models import Author

faker = Faker("pl_PL")

def generate_authors(n: int=10) -> List[Author]:
    authors = []
    for _ in range(n):
        a = Author.objects.create(name=faker.first_name(), last_name=faker.last_name())
        authors.append(a)

    return authors
