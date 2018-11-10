from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Reminder
from .forms import reminderform

# Create your views here.
def index(request):


    return render(request, "my_app/homepage.html")

def reminder(request):
    reminders=Reminder.objects.all()
    context={
        'reminders':reminders
    }
    return render(request,"my_app/reminders.html",context=context)

def details(request,pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'my_app/details.html', {'reminder': reminder})

def add(request):
    if request.method=='POST':
        form=reminderform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            date=form.cleaned_data['date']
            desciption=form.cleaned_data['description']
            Reminder.objects.create(
                name=name,
                date=date,
                description=desciption,
            ).save()
    else:
        form=reminderform
    context={
        'form':form
    }
    return render(request,"my_app/add.html",context=context)

