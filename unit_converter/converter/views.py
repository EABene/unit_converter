from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .conversions import convert

def index(request):
    result = None
    value = request.GET.get('value')
    from_unit = request.GET.get('from_unit')
    to_unit = request.GET.get('to_unit')

    if value:
        result = convert(float(value), from_unit, to_unit)

    return render(request, 'converter/index.html', {'result': result})