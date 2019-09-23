#from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import DataForm
import requests
from .models import Bin1,Bin2,Bin3
from django.utils.dateparse import parse_datetime


def index(request):
    values=Bin1.objects.all()

    count = len(values)
    URL="https://io.adafruit.com/api/v2/giripranay/feeds/bin1/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"
    r = requests.get(url=URL)
    new=r.json()
    count2=len(new)
    if(count!=count2):
        for j in range(0,count2-count):
            i=new[count2-count-j-1]
            temp_date = parse_datetime(i['created_at'])
            obj=Bin1(value=i['value'],date=temp_date)
            obj.save()
    values=Bin1.objects.all()
    count = len(values)
    latest=Bin1.objects.all().order_by('-id')[0]


    values2=Bin2.objects.all()

    coun = len(values2)
    URL="https://io.adafruit.com/api/v2/giripranay/feeds/dustbin1/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"
    r = requests.get(url=URL)
    new=r.json()
    coun2=len(new)
    if(coun!=coun2):
        for j in range(0,coun2-coun):
            i=new[coun2-coun-j-1]
            temp_date = parse_datetime(i['created_at'])
            obj=Bin2(value=i['value'],date=temp_date)
            obj.save()
    values2=Bin2.objects.all()
    coun = len(values2)
    latest2=Bin2.objects.all().order_by('-id')[0]

    values3=Bin3.objects.all()
    cou = len(values3)
    URL="https://io.adafruit.com/api/v2/giripranay/feeds/bin3/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"
    r = requests.get(url=URL)
    new=r.json()
    cou3=len(new)
    if(cou!=cou3):
        for j in range(0,cou3-cou):
            i=new[cou3-cou-j-1]
            temp_date = parse_datetime(i['created_at'])
            obj=Bin3(value=i['value'],date=temp_date)
            obj.save()
    values3=Bin3.objects.all()
    cou = len(values3)
    latest3=Bin3.objects.all().order_by('-id')[0]


    data={'lis':new,'count':count,'count2':count2,'values':values,'latest':latest,'latest2':latest2,'latest3':latest3}

    return render(request,'IOT_app/index.html',data)

def data(request):
    if request.method =='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return redirect('index')
    else:
        form=DataForm()
    return render(request,'IOT_app/data.html',{'form':form})



def bin1(request):
    bills_list=Bin1.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin1.html',data)


def bin2(request):
    bills_list=Bin2.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin2.html',data)

def bin3(request):
    bills_list=Bin3.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin3.html',data)

def maps(request):
    data={}
    return render(request,'IOT_app/maps.html',data)

def graphs(request):

    b1=Bin1.objects.all()
    d={'lis':b1,}
    c1=0
    for row in d['lis']:
        c1 +=row.value

    b2=Bin2.objects.all()
    d2={'lis':b2,}
    c2=0
    for row in d2['lis']:
        c2 +=row.value

    b3=Bin3.objects.all()
    d3={'lis':b3,}
    c3=0
    for row in d3['lis']:
        c3 +=row.value


    data={"bin1":c1 ,"bin2":c2,"bin3":c3,"lis":d3}

    return render(request,'IOT_app/graphs.html',data)

def google(request):
    latest=Bin1.objects.all().order_by('-id')[0]
    latest2=Bin2.objects.all().order_by('-id')[0]
    latest3=Bin3.objects.all().order_by('-id')[0]
    data={'latest':latest,'latest2':latest2,'latest3':latest3}
    return render(request,'IOT_app/google.html',data)
