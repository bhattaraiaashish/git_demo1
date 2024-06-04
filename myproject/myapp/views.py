from django.shortcuts import render
from .models import Person
from django.db.models import Q

# Create your views here.
def person_list(request):
    persons = Person.objects.filter(age__lte=10).values()
    #persons=Person.objects.filter(Q(name__startswith='Aashish') | Q(phone='9876543210')).values()
    #persons=Person.objects.filter(age__gte=10).values()

    
    #for person in persons:
        #print(person.name)
        #print(person.email)
        #print("_______")
    print(persons)    
    context={
        'persons':persons
    }
    return render(request,'person_list.html',context)
