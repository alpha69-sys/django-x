from django.shortcuts import render,get_object_or_404,redirect
from .models import  x
from .forms import x_forum,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')
def x_list(request):
    tweets=  x.objects.all().order_by('-created_at')
    return render(request,'x_list.html',{'x':tweets})
@login_required
def x_create(request):
    if request.method=='POST':
        form = x_forum(request.POST,request.FILES)
        if form.is_valid():
           x= form.save(commit=False)
           x.user=request.user
           x.save()
           return redirect('x_list')
    else:
        form=x_forum()
    return render(request,'x_form.html',{'form':form})

@login_required

def x_edit(request,x_id):
    tweet=get_object_or_404(x,pk=x_id,user=request.user)
    if request.method=='POST':
        form=x_forum(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('x_list')
    else:
        form= x_forum(instance=tweet)
    return render(request,'x_form.html',{'form':form})

@login_required
def x_delete(request,x_id):
    tweet=get_object_or_404(x,pk=x_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('x_list')
    return render(request,'x_delete_confirm.html',{'x':tweet})
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('x_list')
        
    
    else :
        form= UserRegistrationForm()  

    
    return render(request,'registration/register.html',{'form':form})
def x_search(request):
    query=request.GET.get('q')
    if query:
        results=x.objects.filter(text__icontains=query)
    else:
        results=x.objects.none()
    return render(request,'x_list.html',{'x':results,'query':query})
