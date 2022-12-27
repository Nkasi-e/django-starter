from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # context = {
    #    'name':'Nkasi',
    #    'age':'20',
    #    'nationality':'Nigeria'
    # }
    features = Feature.objects.all() # to access all the files in the database admin and it is an array 
    return render(request, 'index.html', {'features': features})

def about(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Commander'
    feature1.details = 'Lets get it done'
    
    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Army'
    feature2.details = 'Lets get it done with'
    
    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'Smith'
    feature3.details = 'Lets get it done off'
    
    feature4 = Feature()
    feature4.id = 4
    feature4.name = 'Controller'
    feature4.details = 'Lets get it done for'
    
    features = [feature1, feature2, feature3, feature4]
 
    return render(request, 'about.html', {'features':features})

def counter(request):
    return render(request, 'counter.html')

def wordcount(request):
    # words = request.GET['words'] when using the get method
    # words = request.POST['words'] # when using the post method
    # number_of_words = len(words.split()) # to get the amount of word present
    posts = [1, 2, 3, 4, 5, 'man', 'woman', 'people']
    return render(request, 'wordcount.html', { 'posts': posts})

"""
Building a registration from using django auth and saving it to our admin
"""

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists(): # checking for existing email
                messages.info(request, 'Email already exist')
                return redirect('registration')
            elif User.objects.filter(username=username).exists(): # checking if username already exists
                messages.info(request, 'username already in use')
                return redirect('registration')
            else:
                # Creating the user if all conditions are met
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not correct')
            return redirect('registration')
    else:
        return render(request, 'registration.html')
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # authenticating user for login
        user = auth.authenticate(username=username, password=password)
        
        # checking if user exist
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk): # Dynamically passing a parameter
    return render(request, 'post.html', {'pk': pk})
        