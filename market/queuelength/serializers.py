from rest_framework import serializers
from .models import store_queue
from .models import store_queue_history

class store_queueSerializer(serializers.ModelSerializer):

    class Meta:
        model= store_queue
        fields= ('store_id', 'queue_id', 'length', 'updated_at', 'threshold', 'threshold_duration')
    

class store_queue_historySerializer(serializers.ModelSerializer):

    class Meta:
        model= store_queue_history
        fields= ('id', 'store_id', 'length', 'updated_at')