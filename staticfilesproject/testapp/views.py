from django.shortcuts import render
def result_view(request):
    return render(request,'testapp/results.html')
