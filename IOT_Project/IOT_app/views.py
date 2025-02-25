from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import DataForm
from .models import Bin1, Bin2, Bin3


def index(request):
    # Fetch latest entry for each bin
    latest_bin1 = Bin1.objects.order_by('-id').first()
    latest_bin2 = Bin2.objects.order_by('-id').first()
    latest_bin3 = Bin3.objects.order_by('-id').first()

    # Fetch all values (only if necessary)
    bin1_values = Bin1.objects.all()
    bin2_values = Bin2.objects.all()
    bin3_values = Bin3.objects.all()

    context = {
        'values': bin1_values,
        'latest': latest_bin1,
        'latest2': latest_bin2,
        'latest3': latest_bin3
    }
    return render(request, 'IOT_app/index.html', context)


def data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DataForm()
    return render(request, 'IOT_app/data.html', {'form': form})


def bin1(request):
    bin1_list = Bin1.objects.all().order_by('-id')
    return render(request, 'IOT_app/bin1.html', {'lis': bin1_list})


def bin2(request):
    bin2_list = Bin2.objects.all().order_by('-id')
    return render(request, 'IOT_app/bin2.html', {'lis': bin2_list})


def bin3(request):
    bin3_list = Bin3.objects.all().order_by('-id')
    return render(request, 'IOT_app/bin3.html', {'lis': bin3_list})


def maps(request):
    return render(request, 'IOT_app/maps.html')


def graphs(request):
    # Aggregate sum of values from each table
    bin1_total = Bin1.objects.aggregate(total=Sum('value'))['total'] or 0
    bin2_total = Bin2.objects.aggregate(total=Sum('value'))['total'] or 0
    bin3_total = Bin3.objects.aggregate(total=Sum('value'))['total'] or 0

    context = {
        "bin1": bin1_total,
        "bin2": bin2_total,
        "bin3": bin3_total
    }
    return render(request, 'IOT_app/graphs.html', context)


def google(request):
    latest_bin1 = Bin1.objects.order_by('-id').first()
    latest_bin2 = Bin2.objects.order_by('-id').first()
    latest_bin3 = Bin3.objects.order_by('-id').first()

    context = {
        'latest': latest_bin1,
        'latest2': latest_bin2,
        'latest3': latest_bin3
    }
    return render(request, 'IOT_app/google.html', context)
