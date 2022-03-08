from django.shortcuts import render


def hw(request):
    return render(request, 'HelloWorld/index.html')
