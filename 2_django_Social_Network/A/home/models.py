from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#آدرس مقاله دیتابیس
#https://www.mongard.ir/articles/176/aunderstanding-database-relations/
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length= 500)
    slug= models.SlugField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        # return self.slug
        return f'{self.slug} - {self.updated}'
