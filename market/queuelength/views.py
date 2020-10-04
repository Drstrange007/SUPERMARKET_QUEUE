from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import store_queue
from .serializers import store_queueSerializer
from django.http import JsonResponse
from .models import store_queue_history
from .serializers import store_queue_historySerializer
from django.utils import timezone

from django.db.models import Avg, Max, Min, Sum

class storeInfoList (APIView):

    def get(self, request, storeId):
        queue1= store_queue.objects.filter(store_id=storeId)
        serializer = store_queueSerializer(queue1, many=True)
        return Response(serializer.data)

    def put(self, request, storeId):
        queue1= store_queue.objects.filter(store_id=storeId).first()
        print("s.ljkf :: " +  str(timezone.now() -queue1.threshold_duration))
        if queue1 in [None, '']:
                return Response(data="Store ID Missing")
        else :
            queue2 = store_queue_history.objects.filter(store_id=storeId,
            updated_at__gte = (timezone.now() - queue1.threshold_duration)).aggregate(Max('length'))
            if queue2['length__max'] in [None, ''] or (queue2['length__max'] - request.data['length']) <= queue1.threshold:
                 serializer = store_queueSerializer(queue1, data=request.data, partial=True)
            else :
                 return Response(data="Change Not Allowed")
                                   

        if serializer.is_valid():
            serializer.save()
            history = store_queue_history(store_id  = storeId , length = request.data['length']) 
            history.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")


    def post(self, request):
        queue1= store_queue.objects.filter(store_id=request.data['store_id']).first()
        serializer = store_queueSerializer(queue1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            history = store_queue_history(store_id  = request.data['store_id'] , length = request.data['length']) 
            history.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")

class storeQueueHistory (APIView):

    def get(self, request, storeId):
        queue1= store_queue_history.objects.filter(store_id=storeId)
        serializer = store_queue_historySerializer(queue1, many=True)
        return Response(serializer.data)

