from django.db import models


# Create your models here.
class Article(models.Model):
    tittle=models.CharField(max_length=250)
    des=models.TextField()
    img=models.ImageField(upload_to='good/')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tittle
    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'
