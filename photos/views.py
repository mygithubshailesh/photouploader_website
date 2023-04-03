from django.shortcuts import render,redirect
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
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
            print(category)
        elif data ['category_new'] != '':
                category,created = Category.objects.get_or_create(name = data['category_new'])
        else :
            category = None

        photo = Photo.objects.create(
                    category = Category,
                    description = data['description'],
                    image = image)
    
        return redirect ('gallery')
      
        """print("data:",data)
        print("image:",image)"""
    contex = {'categories':categories}
    return render(request,'photos/add.html',contex)
