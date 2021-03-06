from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Room(models.Model):
    floor=models.CharField(_('floor'),max_length=255,blank=True,null=True)
    building_name=models.CharField(_('building_name'),max_length=255,blank=True,null=True)
    tiles=models.TextField(_('tiles'),blank=True,null=True)
    formatID=models.CharField(_('formatID'),max_length=255,blank=True,null=True)
    row=models.IntegerField(_('row'),blank=True,null=True,default=0)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["row"]
