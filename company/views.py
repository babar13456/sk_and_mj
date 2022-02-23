from django.shortcuts import render
def home(request):
	return render(request,'index.html')

def signup_page(request):
	return render(request,'signup.html')