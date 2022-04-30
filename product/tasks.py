import random
import string
import requests
from celery import shared_task


def random_int():
    return random.randrange(1000, 100000, 50)


def random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


@shared_task
def create_product():
    requests.post('http://localhost:8000/product/add/', json={'name': random_string(), 'price': random_int()})
