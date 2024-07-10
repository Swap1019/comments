from django.db import models
from user.models import User

class Blog(models.Model):
    blog = models.TextField(verbose_name='content')

class comments(models.Model):
    parent = models.ForeignKey('self',default=None,blank=True,null=True,on_delete=models.SET_NULL,related_name='children',verbose_name="parent")
    user = models.ForeignKey(User,to_field='username',blank=True,null=True,on_delete=models.SET_NULL)
    related_blog = models.ForeignKey(Blog,to_field='id',on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Comment')

    class Meta:
        ordering = ['parent__id']

    def __str__(self):
        return str(self.id)


