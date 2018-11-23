from django.contrib.auth import get_user_model


def get_stub_user():
    return get_user_model().objects.get_or_create(
        email="anonymous@example.com"
    )[0]
