from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'Profile for {self.user.username}'

    def save(self):

        super().save()

        img = Image.open(self.image.path)

        if img.height > 50 or img.width > 50:
            # resize
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.image.path)