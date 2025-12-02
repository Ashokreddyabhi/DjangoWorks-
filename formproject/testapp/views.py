from django.shortcuts import render
from testapp.forms import StudentForm
def student_input_view(request):
    form = StudentForm()
    submitted = False
    name =''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("form validation successfully.......")
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('Marks:',form.cleaned_data['marks'])
            name = form.cleaned_data['name']
            submitted = True
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'name':name})
