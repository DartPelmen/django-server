import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from FLDjangoServer import models
from FLDjangoServer.models import Table1


# Create your views here.
def getAll(request):
    output = []
    out = models.Table1.objects.values()
    for o in out:
        output.append(o)
    return JsonResponse({'table1': output})


@csrf_exempt
def insertRow(request):
    if request.method == 'POST':
        row = json.loads(request.body)
        table = Table1(data1=row['data1'],data2=row['data2'],data3=row['data3'],data4=row['data4'])
        table.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("404")
