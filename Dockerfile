FROM praekeltfoundation/django-bootstrap
ENV DJANGO_SETTINGS_MODULE "seed_identity_store.settings"
RUN ./manage.py collectstatic --noinput
ENV APP_MODULE "seed_identity_store.wsgi:application"
