web: gunicorn project.wsgi
celery: celery -A project._celery:_celery worker -l INFO
beat: celery -A project._celery:_celery beat -l INFO⏎