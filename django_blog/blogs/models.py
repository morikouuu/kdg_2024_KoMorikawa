from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    
    picture = models.ImageField(null=True,blank=True)
    text = models.TextField(blank=True)

    
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,)
    text = models.TextField()
    picture = models.ImageField(null=True,blank=True)
    parent = models.ForeignKey('self', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)

    
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    

    
class Reply(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )
    picture = models.ImageField(null=True,blank=True)
    Reply = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

