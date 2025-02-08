from django.db import models  # type: ignore
from django.contrib.auth.models import User  # Import Django's built-in User model


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to="profile_pics/", default="default.jpg")

#     def __str__(self):
#         return self.user.username
    
class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One user → Many hobbies
    hobby = models.CharField(max_length=200)  # Hobby name
    
def __str__(self):
        return f"{self.user.username} - {self.hobby}"  # Show username and hobby
