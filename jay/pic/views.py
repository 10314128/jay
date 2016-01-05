from django.shortcuts import render

def pic(request):
    return render(request, 'pic/pic.html')