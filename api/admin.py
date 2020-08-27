from django.contrib import admin
from .models import users,blogs,follow,groups,group_members,private_blogs

# Register your models here.

admin.site.register(users)
admin.site.register(blogs)
admin.site.register(follow)
admin.site.register(groups)
admin.site.register(group_members)
admin.site.register(private_blogs)
