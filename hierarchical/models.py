from django.db import models
from django.contrib import admin
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from django.contrib.auth.models import User


# class NewUser(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username


class File(MPTTModel):
    name = models.CharField(max_length=30, unique=True)
    # newuser = models.ForeignKey(NewUser, on_delete=models.CASCADE, default="")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __sts__(self):
        return self.name


admin.site.register(
    File,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

# admin.site.register(NewUser)
