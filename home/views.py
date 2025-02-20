from django.shortcuts import render
from .models import projects
from .models import ticket
def home(request):
    project=projects.objects.all()
    if request.method=='POST':
        name=request.POST.get("contactName")
        email=request.POST.get("contactEmail")
        subject=request.POST.get("contactSubject")
        message=request.POST.get("contactMessage")
        ticket.objects.create(Name=name,email=email,subject=subject,message=message)
    return render(request, 'home/index.html', context={"projects":project})
# Create your views here.
