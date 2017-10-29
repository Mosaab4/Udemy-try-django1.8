from django.shortcuts import render

from .forms import SignUpForm,ContactForm
# Create your views here.
def home(request):
    title = "welcome"
    # if request.user.is_authenticated() :
    #     title = "Welcome %s" %(request.user)
    # else:
    #     title= "Welcome"


    form = SignUpForm(request.POST or None)

    context = {
        "title":title,
        "form":form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        
        # if not instance.full_name == None :
        #     instance.full_name = "mosaab"

        full_name = form.cleaned_data.get("full_name")

        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
    context = {
        "title":"Thank you",
    }

    return render(request,"home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")
        print email,message, full_name

        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        #     print form.cleaned_data.get(key)
    context = {
        "form":form,
    }

    return render(request, "forms.html", context)