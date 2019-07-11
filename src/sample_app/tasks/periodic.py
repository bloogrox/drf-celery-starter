from project._celery import _celery
from .print_hello import print_hello


@_celery.task
def periodic():
    print_hello.delay()
