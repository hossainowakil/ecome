from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='sign_in')
def home(request):
    people = [
        {
            "name":"oakil",
            "age":34,
            "phone":"567899987"
        },
        {
            "name":"imam",
            "age":34,
            "phone":"7899987"
        },
        {
            "name":"najmul",
            "age":45,
            "phone":"99987"
        }

    ]
    my_list = ["apple","mango","banana"]
    context = {
        'people':people,
        'my_list' : my_list
    }
    return render(request , 'management/home.html',context)


@login_required(login_url='sign_in')
def contact(request):
    contacts = Contact.objects.all()
    search = request.GET.get('search')
    if search:
        contacts = Contact.objects.filter(Q (name=search)  | Q(phone=search))

    context = {
        'contacts':contacts
    }
    
    return render(request , 'management/contact.html',context)


def detail(request,id):
    contact = Contact.objects.get(id=id)
    context ={
        'contact': contact
    }
    return render(request,'management/detail.html',context)

@login_required(login_url='sign_in')
def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone= request.POST.get('phone')
        address = request.POST.get('address')
        if name and age and phone and address:
                 Contact.objects.create(
                     name = name,
                     age = age,
                     phone = phone,
                     address = address
                 )
                 messages.success(request, f"contact added {name} successfull")
                 
                 return redirect('contact')
        else:
            messages.error(request, f"contact  {name} not added")
             
         
         
        
              
    return render(request, 'management/add_contact.html')


def delete_contact(request,id):
     contact = Contact.objects.get(id=id)
     contact.delete()
     messages.success(request, f"contact delete successful")
     return redirect('contact')


def edit_contact(request, id):
     
     contact = Contact.objects.get(id=id)
     if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone= request.POST.get('phone')
        address = request.POST.get('address')
    
        contact.name=name
        contact.age = age
        contact.phone= phone
        contact.address= address
        contact.save()
        messages.success(request, f"contact edit successful")
        return redirect('contact')
     context = {
          'contact' : contact
     }
     return render(request, 'management/edit_contact.html',context)

def profile(request):
     return render(request, 'management/profile.html')

def sign_in(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          print(username,password)

          user =authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               messages.error(request, 'invalied username or password')
          



     return render(request, 'management/sign_in.html')

def sign_up(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('password')
          confirm_password=request.POST.get('confrim_password')
          if password != confirm_password:
               messages.error(request, 'password does not match')
               return redirect('sign_up')
          else:
               user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
               )
               messages.success(request,'added successful')
               return redirect('sign_in')
     return render(request, 'management/sign_up.html')
