from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    teaser = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='test.jpeg', blank=True)
    copyright = models.CharField(max_length=75, blank=True)
    category = models.ForeignKey(
            "Category",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            default=None,
            related_name="posts",
        )
    def __str__(self):
        return self.title
    
    def get_related_posts(self, limit=3):
        return Post.objects.all().exclude(id=self.id).distinct()[:limit]

class Category(models.Model):
    title = models.CharField(max_length=75) 
    
    def __str__(self):
        return self.title