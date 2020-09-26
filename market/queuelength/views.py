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


class store_queueList (APIView):

    def get(self, request):
        queue1= store_queue.objects.all()
        serializer = store_queueSerializer(queue1, many=True)
        return Response(serializer.data)

    def post(self):
        pass



class storeInfoList (APIView):

    def get(self, request, storeId):
        queue1= store_queue.objects.filter(store_id=storeId)
        serializer = store_queueSerializer(queue1, many=True)
        return Response(serializer.data)

    def put(self, request, storeId):
        queue1= store_queue.objects.filter(store_id=storeId).first()
        if queue1 in [None, '']:
                return Response(data="Store ID Missing")
        serializer = store_queueSerializer(queue1, data=request.data, partial=True)
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

