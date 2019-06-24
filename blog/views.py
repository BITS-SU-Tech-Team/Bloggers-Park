from django.shortcuts import render
from django.http import Http404
from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView

def index(request):
    return render(request, 'index.html')

def bloglist(request):
    blog = Blog.objects.filter(status=1).order_by('-created_on')
    return render(request, 'bloglist.html', {'blogs': blog})

def blog(request, slug):
    #try and except
    try:
        blog = Blog.objects.get(slug=slug)
        hit_count = HitCount.objects.get_for_object(blog)
        print(HitCountMixin.hit_count(request, hit_count))

    except Blog.DoesNotExist:
        raise Http404

    return render(request, 'blog.html', {'blog': blog})

# @login_required
# def blogform(request):
#
#     ImageFormSet = modelformset_factory(Image,
#                                         form=ImageForm, extra=3)
#     #'extra' means the number of photos that you can upload   ^
#     if request.method == 'POST':
#
#         blogForm = BlogForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES,
#                                queryset=Image.objects.none())
#
#
#         if blogForm.is_valid() and formset.is_valid():
#             blog_form = blogForm.save(commit=False)
#             blog_form.author = request.user
#             blog_form.save()
#
#             for form in formset.cleaned_data:
#                 #this helps to not crash if the user
#                 #do not upload all the photos
#                 if form:
#                     image = form['image']
#                     photo = Image(blog=blog_form, image=image)
#                     photo.save()
#             return render(request, 'bloglist.html')
#         else:
#             print(blogForm.errors, formset.errors)
#     else:
#         blogForm = BlogForm()
#         formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'blogform.html',
#                   {'blogForm': blogForm, 'formset': formset})

# @login_required
# def blogform(request):
#     form = BlogForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         print(form.cleaned_data['title'])
#
#     return render(request, 'blogform.html', {'form': form})
