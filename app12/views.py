
from django.shortcuts import render
from .models import listing

# Create your views here.
def main(request):
    return render (request,"static/index.html")

def home(request):
    return render(request, "static/index.html")

def opp(request):
    titles =listing.objects.all()
    return render(request, 'static/opp.html', {
        "titles":titles,
    })

def sub(request):
    return render(request, "static/sub.html")