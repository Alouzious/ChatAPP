from django.db import models
from django.contrib.auth.models import User

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friend_requests')
    is_accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({'Accepted' if self.is_accepted else 'Pending'})"
    