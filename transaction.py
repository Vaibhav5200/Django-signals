import transaction
from django.db import IntegrityError
from django.dispatch import receiver, signal

# Define a signal
my_signal = signal(providing_args=["sender", "message"])

# Define a receiver for the signal
@receiver(my_signal)
def my_receiver(sender, message, **kwargs):
    print(f"Received signal: {message}...")
    try:
        # Attempt to create a model instance with invalid data
        MyModel.objects.create(name=None)
    except IntegrityError:
        print("Error: IntegrityError occurred in signal receiver")

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=255)

# Send the signal within a transaction
def send_signal():
    print("Sending signal...")
    with transaction.atomic():
        try:
            # Create a model instance
            MyModel.objects.create(name="Valid instance")
            # Send the signal
            my_signal.send(sender="sender", message="Hello, world!")
            # Simulate a failure
            raise ValueError("Simulated failure")
        except ValueError:
            print("Error: Simulated failure occurred")

# Test the signal
send_signal()

"""When you run this code, you'll see that the IntegrityError exception is caught 
in the signal receiver, but the ValueError exception is not caught. 
This is because the signal receiver runs in a separate database transaction."""
  
  # OUTPUT
  
""" Sending signal...
Received signal: Hello, world!...
Error: IntegrityError occurred in signal receiver
Error: Simulated failure occurred"""

"""As you can see, the IntegrityError exception is caught in the signal receiver, 
but the ValueError exception is not caught.This confirms that Django signals do not 
run in the same database transaction as the caller."""