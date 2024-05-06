from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Comment
from cars.models import Car


# Create your views here.
@require_POST
def create(req, pk):
    comment=Comment(
        car_id=pk,
        context=req.POST['context']
    )
    comment.save()
    comments = Comment.objects.all().filter(car_id=pk).order_by('-id')

    return render(req, 'comments/comment.html', {'comments':comments})

@require_POST
def delete(req, pk):
    comment = get_object_or_404(Comment, pk=pk)
    breakpoint()
    comment.delete()
    
    return HttpResponse('')
    # return render(req, 'cars/show.html', {'car':car, 'comments':comments})
    # comments = Comment.objects.all().filter(car_id=pk).order_by('-id')

    # return render(req, 'comments/comment.html', {'comments':comments})