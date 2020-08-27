from django.db import models


# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    aboutme=models.TextField(default=None)
    profileimageurl=models.TextField(default=None)
    blogswritten=models.PositiveIntegerField(default=0)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    token=models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.username

class blogs(models.Model):
    blogimageurl=models.TextField()
    title=models.CharField(max_length=1000)
    category=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    public=models.BooleanField()
    writtenby=models.ForeignKey(users,to_field='id',default=None,on_delete=models.CASCADE)
    content=models.TextField(default="")


class follow(models.Model):
    follower=models.ForeignKey(users,to_field='id',on_delete=models.CASCADE,related_name='follower_id')
    following=models.ForeignKey(users,to_field='id',on_delete=models.CASCADE,related_name='following_id')


class groups(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class group_members(models.Model):
    user=models.ForeignKey(users,to_field='id',default=None,on_delete=models.CASCADE)
    group=models.ForeignKey(groups,to_field='id',default=None,on_delete=models.CASCADE)

class private_blogs(models.Model):
    #Do not insert public blogs here .Understood sir 
    blogid=models.ForeignKey(blogs,to_field='id',default=None,on_delete=models.CASCADE,null=True)
    groupid=models.ForeignKey(groups,to_field='id',default=None,null=True,on_delete=models.CASCADE)
