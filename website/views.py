from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from . import sentimeter
from .models import Sentiment



def index(request):
    user_input = userinput()
    return render(request, "index.html", {'input_hastag': user_input})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['q']
        print (input_hastag)
        data = sentimeter.primary(input_hastag)
        d=Sentiment.objects.create(input=user_input,pos=data[1][1],neg=data[3][1],neu=data[2][1])
        d.save()
        return render(request, "result.html", {'data': data})
    return render(request, "index.html", {'input_hastag': user_input})