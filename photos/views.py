from django.shortcuts import render
from .models import Category,Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    contex = {'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',contex)

def viewphotos(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request,'photos/photos.html',{'photo':photos})

def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print('data:',data)  
        print('image:',image) 

    contex = {'categories':categories}
    return render(request,'photos/add.html',contex)
