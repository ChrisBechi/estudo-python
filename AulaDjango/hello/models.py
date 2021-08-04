from django.db import models
import uuid

# Create your models here.
class Movies(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('filme', max_length=100)
  image = models.ImageField(verbose_name='Capa', blank=True, null=True)

class Meta:
  db_table = 'movies'

def __str__(self):
    return self.name

