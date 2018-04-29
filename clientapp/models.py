from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class GCRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='request_images/%Y/%m/',default='images/img.png')
    latitude=models.DecimalField(max_digits=40, decimal_places=20,default=0)
    longitde=models.DecimalField(max_digits=40, decimal_places=20,default=0)
    Choices=(('Not responded yet','Not responded yet'),
             ('Accepted','Accepted'),
             ('Rejected','Rejected'))
    status=models.CharField(max_length=20,choices=Choices,default='Not responded yet')
    requested_on=models.DateField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name='Garbage Collection Request'

@receiver(post_delete, sender=GCRequest)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
