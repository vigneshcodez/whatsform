from django.shortcuts import render
from . models import plan

# Create your views here.


def index(request):
        yearly = plan.objects.get(id=1)
        return render(request, 'app/index.html', {'x': yearly})

def index2(request):
        monthly = plan.objects.get(id=2)
        return render(request, 'app/index.html', {'x': monthly})