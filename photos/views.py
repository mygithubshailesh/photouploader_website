from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Category,Photo
from .forms import Sing_up,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
         photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(Category__name =category) 
    
    categories = Category.objects.all()
   
    contex = {'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',contex)

def viewphotos(request, pk):
    photos = Photo.objects.get(id=pk)
      
    return render(request,'photos/photos.html',{'photo':photos})

def addphoto(request):
   if request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == 'POST':
            data = request.POST
            image = request.FILES.get('image')
            if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
                print(category)
            elif data ['category_new'] != '':
                    category,created = Category.objects.get_or_create(name = data['category_new'])
            else :
                category = None

            photo = Photo.objects.create(
                        Category = category,
                        description = data['description'],
                        Image =   image)
        
            return redirect ('gallery')
        contex = {'categories':categories}
        return render(request,'photos/add.html',contex)
   else:
       return HttpResponseRedirect('/signup/')

def signup(request):
     if request.method == "POST":
          fm = Sing_up(request.POST)
          if fm.is_valid():
            fm.save()
            return HttpResponseRedirect ("/login/")
     else:
          fm = Sing_up()
     return render(request,'photos/signup.html',{'fm':fm})

def user_login(request):
     if request.method == "POST":
          form = LoginForm(request=request, data=request.POST)
          if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully !!')
                return HttpResponseRedirect('/')
     else:
        form = LoginForm()
     return render(request, 'photos/login.html', {'form':form})


def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

def delete_photo(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Photo.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')
  else:
    return HttpResponseRedirect('/login/')
            

     
