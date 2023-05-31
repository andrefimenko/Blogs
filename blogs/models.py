from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog."""
    blog_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.blog_name

class Post(models.Model):
    """A post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Return a simple string represtning the post."""
        return f"{self.text[:50]}..."
