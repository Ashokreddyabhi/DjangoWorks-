from django.shortcuts import render
import datetime
def wish(request):
    date = datetime.datetime.now()
    msg = 'hello every one very very good'
    h = int(date.strftime( '%H '))
    if h <=12:
        msg +='morning'
    elif h < 16:
        msg +='aftrnoon'
    elif h <=21:
        msg += 'even'
    else:
        msg +='GN'
    name = 'abhi'
    rollno = 18216
    marks = 99
    my_dict = {'insert_date':date,'insert_msg':msg,'insert_name':name,'rollno':rollno,'marks':marks}
    return render(request,'tempapp/wish.html',context=my_dict)
  
  