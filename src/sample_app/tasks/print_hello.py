from project._celery import _celery


@_celery.task
def print_hello():
    print("Hello")
