from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=240)
    photo=models.ImageField(upload_to="photos/",blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'
    

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tweet_detail', args=[str(self.id)])
    
    
    # followers and following feature code 
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    followers = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return self.user.username

    def follow(self, user):
        """Follow a user"""
        self.followers.add(user)

    def unfollow(self, user):
        """Unfollow a user"""
        self.followers.remove(user)

    def is_following(self, user):
        """Check if the current user is following another user"""
        return self.followers.filter(id=user.id).exists()

    def followers_count(self):
        """Return number of followers"""
        return self.followers.count()

    def following_count(self):
        """Return number of users this user follows"""
        return self.user.following.count()
