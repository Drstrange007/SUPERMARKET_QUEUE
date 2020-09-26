from django.db import models

class store_queue(models.Model):
    store_id = models.CharField(max_length=255,primary_key=True)
    queue_id = models.CharField(max_length=255)
    length = models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now_add= True,null=True)


class store_queue_history(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=255)
    length = models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now_add= True,null=True)

    
