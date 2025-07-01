from django.shortcuts import render
from django.http import HttpResponse
import datetime
from myapptock.models import Cust
from django.contrib import messages

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


def cust_profile(request):
    cust = {
        'name': 'Baramee',
        'lastname': 'Punyafuaen',
    }
    custrecode = Cust()
    custrecode.name = 'Baramee'
    custrecode.lastname = 'Punyafuaen'
    try:
        custrecode.save()
        print("Customer record saved successfully.")
        messages.success(request, "Customer record saved successfully.")
    except Exception as e:
        print(f"Error saving customer record: {e}")
        messages.error(request, f"Error saving customer record: {e}")
    finally:
        return render(request, 'cust_profile.html', cust)


def get_cust_profile(request):      
    try:
        custs = list(Cust.objects.values('name', 'lastname'))
        messages.success(request, f"Customer found: {custs}")
    except Cust.DoesNotExist:
        print("Customer not found.")
        messages.error(request, "Customer not found.")
        return render(request, 'cust_profile_filter.html', {'custs': []})
    return render(request, 'cust_profile_filter.html', {'custs': custs})