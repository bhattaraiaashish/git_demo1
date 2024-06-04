from django.shortcuts import HttpResponse,render
from random import randint

def index(request):
    random_value= randint(101,999)
    return HttpResponse(f"<h1>Hello Welcome to Django</h1> your Id is {random_value}")


def contact(request):
    name="AASHISH"
    phone="9876543210"
    return HttpResponse(f"<center><h1>This is a contact page</h1> <p> Name: {name}</p> <p>Contact No: {phone}</p><center>")

def home(request):
    return HttpResponse(f"<center><h1>Welcome to the home page</h1><center>")

def about(request):
    return HttpResponse(f"<center><h1>Welcome to the about page</h1><center>")

def services(request):
    services=['Digital Marketing','SEO',"Content Writing"]
    services_data=''.join(services)
    print(services_data)
    return HttpResponse("<h1>Services</h1> <p>{services_data}</p>")

def profile_page(request,id,id1):
    #fetch user from database ussing the id
    print(id)
    return HttpResponse(f"<h1>Profile Page of #{id+id1}</h1>")

def index_page(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if username is not None and password is not None:
        user_data = f"Thanks for submitting! {username} - {password}"
        return HttpResponse(user_data)
    context={
        'name':'RAM',
        'age':55,
        'is_married':False,
        'skills':["python","django","flask"]
    }
    return render(request, 'index.html',context)