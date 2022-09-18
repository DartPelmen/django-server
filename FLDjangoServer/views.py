import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from FLDjangoServer import models
from FLDjangoServer.models import Table1


# Create your views here.
def getAll(request):
    output = []
    out = models.Table1.objects.filter(id=1).values()
    return JsonResponse({"data1": out[0]['data1']})


@csrf_exempt
def insertRow(request):
    if request.method == 'POST':
        row = json.loads(request.body)
        if request.body != None:
            return JsonResponse({"status": "INVALID INPUT"})
        origin = models.Table1.objects.filter(id=1).values()[0]
        origin['data1'] = row['data1']
        table = Table1(id=1, data1=row['data1'], data2=origin['data2'], data3=origin['data3'], data4=origin['data4'])
        table.save()
        return JsonResponse({"status": "OK"})
    else:
        return JsonResponse({"status": "NOT POST"})
