# views.py

from django.contrib.auth.models import User

def create_user_view(request):
    print("View started")
    User.objects.create(username='testuser')  # This will trigger the post_save signal for User
    print("View finished")
