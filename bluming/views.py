from django.shortcuts import render

def halamansatu(request):
    return render(request, 'Halamanasatu.html')

def halamandua(request):
    return render(request, 'halamandua.html')
# Create your views here.
