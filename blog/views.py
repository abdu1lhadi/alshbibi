from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewCustomers

# Create your views here.

def home(request):
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = NewCustomers()
    else:
        comment_form = NewCustomers()
    context = {
        'title': 'HOME',
        'comment_form': comment_form,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT US'})

def coffee(request):
    return render(request, 'blog/coffee_shop.html', {'title': 'coffee'})

def course(request):
    return render(request, 'blog/course_malaysia.html', {'title': 'course'})

def europeClassc(request):
    return render(request, 'blog/Eur_a_classc.html', {'title': 'europeClassc'})

def external(request):
    return render(request, 'blog/External_design.html', {'title': 'ABOUT US'})

def interior(request):
    return render(request, 'blog/ineterior_decorations.html', {'title': 'interior'})

def specialWomen(request):
    return render(request, 'blog/special_women.html', {'title': 'specialWomen'})

def dyes(request):
    return render(request, 'blog/specialty_dyes.html', {'title': 'dyes'})

def upgrading(request):
    return render(request, 'blog/upgrading _engines.html', {'title': 'upgrading'})

def allcars(request):
    return render(request, 'blog/allcars.html', {'title': 'allcars'})


