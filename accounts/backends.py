from django.contrib.auth.models import User
from django.db.models import Q


class EmailAuth:
    """Authenticate user by an exact match on email and password"""

    def authenticate(self, username_or_email=None, password=None):
        """
        Get an instance of User using the supplied username
        or email and verify the password
        """
        try:
            # Filter all users by searching for a match by username/ email.
            print('\n\n EmailAuth username or email', username_or_email)
            # user = User.objects.get(email=username)
            users = User.objects.filter(
                Q(username__exact=username_or_email) |
                Q(email__exact=username_or_email)
            )
            if not users:
                return None
            print('\n\n Users', users)
            user = users[0]
            print('\n\n User', user)
            if user.check_password():
                print('password ok')
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Used by Django auth system to retrieve user instance"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
