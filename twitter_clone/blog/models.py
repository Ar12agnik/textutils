from django.db import models

# Create your models here.
class posts(models.Model):
    tweet_id=models.AutoField
    author_name =models.CharField(max_length=40)
    content=models.CharField(max_length=300)
    pub_date =models.DateField(auto_now_add=True)