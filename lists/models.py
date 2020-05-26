from django.db import models
class List(models.Model): # models.Model包含save()
    pass

class Item(models.Model):
    text = models.TextField(default='')
    # list = models.TextField(default='') # 'List object (1)' != <List: List object (1)>
    list = models.ForeignKey(List,on_delete=models.CASCADE,default=None)


