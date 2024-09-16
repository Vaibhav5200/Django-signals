import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Define the signal handler
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler is running in thread: {threading.current_thread().name}")

# Simulate the save operation which triggers the post_save signal
def save_user():
    print(f"Calling code is running in thread: {threading.current_thread().name}")
    user = User(username='vaibhav', email='vaibhav@example.com')
    user.save()

if __name__ == "__main__":
    save_user()
