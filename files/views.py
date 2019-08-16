from django.shortcuts import render

def car_list(request):
    return render(request, 'files/car_list.html', {})