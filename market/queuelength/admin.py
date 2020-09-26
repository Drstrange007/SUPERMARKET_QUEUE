from django.contrib import admin
from .models import store_queue
from .models import store_queue_history

admin.site.register(store_queue)
admin.site.register(store_queue_history)

