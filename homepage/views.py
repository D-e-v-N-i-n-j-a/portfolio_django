from django.shortcuts import render
from .models import Projects,BackEndLanguages,ServerLanguages,FrondEndLanguages,NonTechnologySkill
# Create your views here.


def homepage(request):
    projects = Projects.objects.all() 
    backEndLanguages = BackEndLanguages.objects.all()
    frontEnd = FrondEndLanguages.objects.all()
    server = ServerLanguages.objects.all()
    skills = NonTechnologySkill.objects.all()
    return render (request,'index.html',{"projects":projects,'backendSkills':backEndLanguages,'frondEndSkills':frontEnd,'server':server,'personalSkills':skills})


 

 

