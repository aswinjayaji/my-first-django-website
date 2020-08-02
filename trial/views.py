from django.shortcuts import render,get_object_or_404,redirect
from .models import Trial
from .forms import ProductForm,RawProductForm

def create_view(request):
    form=RawProductForm()
    if request.method=="POST":
      form=RawProductForm(request.POST or None)
      if form.is_valid():
          print(form.cleaned_data)
          Trial.objects.create(**form.cleaned_data)
      else:
          print(form.errors)
    queryset=Trial.objects.all() 
    context ={
        'form':form,
        'list':queryset
    }
    return render(request,"detail/form.html",context)
def home_view(request):
    obj=Trial.objects.get(id=1)
    context ={
        'object':obj
    }
    return render(request,"detail/details.html",context)
def list_view(request):
    queryset=Trial.objects.all()    
    context ={
        "list":queryset
    }
    return render(request,"detail/list.html",context)

def dynamic_view(request,id):
    obj=Trial.objects.get(id=id)
    context={
        "dynamic":obj
    }
    return render(request,"detail/dynamic.html",context)

def delete_view(request,id):
    obj=get_object_or_404(Trial,id=id)
    if request.method=="POST":
      obj.delete()
      return redirect('../../')
    context ={
        "object":obj
    }
    return render(request,"detail/delete.html",context)
def contact_view(request):
    return render(request,"contacts.html")