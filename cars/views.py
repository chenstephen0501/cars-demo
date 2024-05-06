from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from .models import Car
from comments.models import Comment


# Create your views here.

def index(req):
    cars = Car.objects.all()
    return render(req, 'cars/index.html', {'cars':cars})

def new(req):
    return render(req, 'cars/new.html')

@require_POST
def add(req):
    car = Car(
        name=req.POST['name'],
        color=req.POST['color'],
        brand=req.POST['brand'],
        style_body=req.POST['style_body'],
        price=req.POST['price'],
        description=req.POST['description'],
    )
    messages.success(req, '新增成功')
    car.save()

    return redirect('cars:index')

def show(req, pk):
    car = get_object_or_404(Car, pk=pk)

    comments = Comment.objects.all().filter(car_id=car.id).order_by('-id')

    
    if req.method == 'POST':
        car.name=req.POST['name']
        car.color=req.POST['color']
        car.brand=req.POST['brand']
        car.style_body=req.POST['style_body']
        car.price=req.POST['price']
        car.description=req.POST['description']
        car.save()
        messages.success(req, '編輯成功')

        return redirect('cars:show', pk=car.id)
    else:
        return render(req, 'cars/show.html', {'car':car, 'comments':comments})
        # return render(req, 'cars/show.html', {'car':car})
    
def edit(req, pk):
    car = get_object_or_404(Car, pk=pk)

    return render(req, 'cars/edit.html', {'car':car})    

@require_POST
def delete(req, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    messages.error(req, '刪除成功')

    return redirect('cars:index')
