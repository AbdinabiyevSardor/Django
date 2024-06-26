from .models import Trainer,Contact
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .bot import send_message

def home_view(request):
    trainers = Trainer.objects.all()
    context = {"trainers": trainers}
    
    
    return render(request, "index.html", context=context)
    

def trainer_view(request):
    return render(request, "trainer.html")

def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
                    
    else:
        contact = Contact.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]
            print(name,email,phone_number,description)
            send_message(name,email,phone_number,description)
            
            form.save()
            messages.success(request, "Sizning tekstingiz adminga yuborildi!!!")
            form = ContactForm()
            
            # print(name,email,phone_number,description)
 
    context = {"form": form}
    
    
    return render(request, "contact.html", context=context)

def why_view(request):
    return render(request, "why.html")


def base_view(request):
    return render(request,"base.html")

