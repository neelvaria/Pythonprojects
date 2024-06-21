from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def addcategory(request):
    return render(request, 'addcategory.html')

def completed(request):
    return render(request, 'completed.html')

def edit(request):
    return render(request, 'edit.html')

def forgetpassword(request):
    return render(request, 'forgetpassword.html')

def profile(request):
    return render(request, 'profile.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def tasks_pdf(request):
    return render(request, 'tasks_pdf.html')