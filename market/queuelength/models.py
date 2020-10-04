from django.db import models
from collections import deque 

class store_queue(models.Model):
    store_id = models.CharField(max_length=255,primary_key=True)
    queue_id = models.CharField(max_length=255)
    length = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add= True,null=True)
    threshold = models.IntegerField()
    threshold_duration = models.DurationField()


class store_queue_history(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=255)
    length = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add= True,null=True)




    
