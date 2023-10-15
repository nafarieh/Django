from django.contrib.auth.models import User

class EmailBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, use_id):
        try:
            return User.objects.get(pk = use_id)
        except User.DoesNotExist:
            return None


