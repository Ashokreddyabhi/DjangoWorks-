from django.shortcuts import render
def homepage_view(request):
    return render(request,'testapp/index.html')
from testapp.models import HydJobs
def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)
from testapp.models import BengJobs
def bengjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/bengjobs.html',my_dict)
from testapp.models import ChennaiJobs
def chennaijobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/chennaijobs.html',my_dict)
