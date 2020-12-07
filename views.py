from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.apps import apps
from . import models


def api_handler(request, model=None, pk=None):
    if not model:
        allmodels = apps.get_app_config('trial').get_models()
        names = [type(model).__name__ for model in allmodels]
        return JsonResponse({'result': names})
    model = getattr(models, model.capitalize())
    if pk is None:  # Can primary keys even be zero?
        result = model.objects.all()
    else:
        #result = get_object_or_404(model, pk)
        result = model.objects.filter(pk=pk)
    result = serialize('json', result)
    # Why can't JsonResponse serialize `result` by itself?
    return JsonResponse({'result': result})
