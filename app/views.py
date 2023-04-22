from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is inserted successfully!!')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('Webpage is inserted successfully!!')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ARO=AccessRecordForm()
    d={'ARO':ARO}
    if request.method=='POST':
        ARD=AccessRecordForm(request.POST)
        ARD.save()
        return HttpResponse('insert AccessRecord successfully!!')
    return render(request,'insert_access.html',d)