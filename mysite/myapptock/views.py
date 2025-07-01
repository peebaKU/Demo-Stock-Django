from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("<h1>Welcome to homepage</h1>")

def show_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

def my_template_view(request):
    return render(request, 'MyTemplates.html')


def my_template_view2(request):
    template_var = {
        'name': 'Baramee',
        'surname': 'Punyafuaen',
        'tel': "123-456-7890",
    }
    return render(request, 'MyTemplates2.html', template_var)