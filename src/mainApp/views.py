from django.shortcuts import render
from .forms import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)




# Create your views here.

def login_function(request):
	title="You are loged in"
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		login(request,user)
	if request.user.is_authenticated():
		users_list=User.objects.filter(~Q(username=request.user.username))

		paginator = Paginator(users_list, 10) # Show 25 contacts per page

		page = request.GET.get('page')

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		src1='"https://tokbox.com/embed/embed/ot-embed.js?embedId=d093d3aa-342a-4f78-9f6e-3f4f7e59dda4&room='
		src=src1+request.user.username+'"'
		print(src)
		return render(request,"check.html",{"users":users,"src":src})
	return render(request,"login.html",{"form":form})

def registration(request):
	form1=RegistrationForm(request.POST or None)
	form2=UserInfoForm(request.POST or None)
	context={"form1":form1,"form2":form2}
	if form1.is_valid():
		title='You are registered successfully!'
		user=form1.save(commit=False)
		password=form1.cleaned_data.get('password')
		username=form1.cleaned_data.get('username')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
		userprofile=form2.save(commit=False)
		# userprofile.User=username
		userprofile.user_id=request.user.id
		t=userprofile.save()

	if(request.user.is_authenticated()):
		users_list=User.objects.filter(~Q(username=request.user.username))

		paginator = Paginator(users_list, 10) # Show 25 contacts per page

		page = request.GET.get('page')

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		src1='"https://tokbox.com/embed/embed/ot-embed.js?embedId=d093d3aa-342a-4f78-9f6e-3f4f7e59dda4&room='
		src=src1+request.user.username+'"'
		print(src)
		return render(request,"check.html",{"users":users,"src":src})
	return render(request,"registration.html",context)

def deleteBookFromCart(request,id=None):
	book=''
	if(request.user.is_authenticated()):
		bookd=Book.objects.get(id=id)
		bookd.delete()
		book=Book.objects.filter()
	return render(request,"show.html" ,{"book":book})

def addToCart(request,Book_id=None):
	#print(request.user.id)
	#cartObj=Cart.objects.filter(Book_id=Book_id,user_id=request.user.id)
	#Quantity=1;
	book=''
	if(request.user.is_authenticated()):
		book=Book.objects.filter()
		cartObject=Cart()
		cartObject.UserId_id=request.user.id
		print(cartObject.UserId)
		# cartObject.Quantity=1;
		cartObject.BookId_id=Book_id
		cartObject.save()
		#check=0
	return render(request,"show.html" ,{"book":book})



def show_data(request):
	form=LoginForm(request.POST or None)
	if(request.user.is_authenticated()):
		return render(request,"show.html",{})
	return render(request,"login.html",{"form":form})

def chatroom(request,Uname=None):
	form=LoginForm(request.POST or None)
	if request.user.is_authenticated():
		users_list=User.objects.filter(~Q(username=request.user.username))

		paginator = Paginator(users_list, 10) # Show 25 contacts per page

		page = request.GET.get('page')

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)


		src1='"https://tokbox.com/embed/embed/ot-embed.js?embedId=d093d3aa-342a-4f78-9f6e-3f4f7e59dda4&room='
		src=src1+Uname+'"'
		#print(src)
		return render(request,"check.html",{"users":users,"src":src})
	return render(request,"login.html",{"form":form})
