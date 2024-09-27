from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
from django.db.models import Avg, Count

class Category(models.Model):
    name = models.CharField(unique=True, max_length=300)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('category', 'name')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Spot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=300)
    sub_category = models.ForeignKey(SubCategory, related_name='spots', on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, related_name='uploaded_spots', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Add the date when spot is created
    updated_at = models.DateTimeField(auto_now=True) # update the date when last modification happens
    visited_users = models.ManyToManyField(User, related_name='visited_spots', blank=True)
    favorite_users = models.ManyToManyField(User, related_name='favorite_spots', blank=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
        unique_together = ('name', 'uploaded_by', 'city')
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 0


class ForumComments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_comments')
    spot = models.ForeignKey(Spot, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Comment for Spot {self.spot.name} - by {self.posted_by}"


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spot = models.ForeignKey(Spot, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()  
    review_text = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'spot')
    
    def __str__(self):
        return f"Review of {self.spot.name} by {self.user.username} - Rating: {self.rating}"
