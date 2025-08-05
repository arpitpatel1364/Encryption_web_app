from django.db import models
from django.contrib.auth.models import User
from django.core.signing import Signer
import secrets
import json


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    key = models.CharField(max_length=32, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_channels')
    encrypted_custom_map = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def get_custom_map(self):
        """Decrypt and return the custom map"""
        signer = Signer()
        try:
            return json.loads(signer.unsign(self.encrypted_custom_map))
        except:
            return self.generate_default_map()

    def set_custom_map(self, custom_map):
        """Encrypt and store the custom map"""
        signer = Signer()
        self.encrypted_custom_map = signer.sign(json.dumps(custom_map))

    def generate_default_map(self):
        """Generate default custom map"""
        return {
            'a': 1111, 'b': 5411, 'c': 6888, 'd': 6666, 'e': 2091,
            'f': 3101, 'g': 6212, 'h': 7480, 'i': 1021, 'j': 5090,
            'k': 2780, 'l': 9710, 'm': 8301, 'n': 6571, 'o': 3551,
            'p': 4201, 'q': 3441, 'r': 4910, 's': 7010, 't': 3912,
            'u': 8421, 'v': 8120, 'w': 6630, 'x': 7021, 'y': 4530,
            'z': 9780, ' ': 1119, '.': 9998, ',': 8889, '!': 7779,
            '?': 6670, "'": 7777, '0': 1000, '1': 2000, '2': 3000,
            '3': 4000, '4': 5000, '5': 6000, '6': 7000, '7': 8000,
            '8': 9000, '9': 1500
        }

    def __str__(self):
        return self.name


class ChannelMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'channel')

    def __str__(self):
        return f"{self.user.username} in {self.channel.name}"


class EncryptedMessage(models.Model):
    encrypted_data = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Message in {self.channel.name} by {self.created_by.username}"