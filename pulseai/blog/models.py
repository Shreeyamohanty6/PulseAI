from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogCategory(models.Model):
  category = models.CharField(max_length=255)

  class Meta:
    verbose_name_plural = "Blog Categories"

  def __str__(self):
    return self.category
  

class Blog(models.Model):
  category=models.ForeignKey(BlogCategory, on_delete=models.DO_NOTHING)
  title=models.CharField(max_length=500)
  content=models.TextField()
  primary_photo = models.ImageField(upload_to="blog_images")
  yt_video_id = models.CharField(max_length=255,blank=True)
  publish=models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  

# class Comment(models.Model):
#     blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
#     author = models.CharField(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     rating = models.PositiveSmallIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comment by {self.author} on {self.blog}'

class Comment(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.blog.title+" "+self.comment
    
