from django.shortcuts import render,redirect,HttpResponse,get_object_or_404, redirect
from blog.models import Blog,BlogCategory, Comment
#from .form import CommentForm

# Create your views here.
def index(request):
    #return HttpResponse("Hello World !!")
    return render(request,'blog/index.html')

def about(request):
    #return HttpResponse("<h1>About US</h1>")
    return render(request,'blog/about.html')

def contact(request):
    mobile=9692215902
    email="pulseai@gmail.com"
    a=10
    b=10
    languages=['C','C++','Java','Python']
    blog={
        "title":"Blog Title",
        "author":"John",
        "content":"Blog Details"
    }
    students=[
        {"roll":1,"name":"Smith","cgpa":9.4},
        {"roll":2,"name":"Sara","cgpa":8.4},
        {"roll":3,"name":"Tom","cgpa":9.5},
        {"roll":4,"name":"Spike","cgpa":7.9},
        {"roll":5,"name":"Saran","cgpa":9.9},
    ]
    context= {
        "mob":mobile,
        "email":email,
        "a": a,
        "b": b,
        'languages': languages,
        'blog':blog,
        'students':students,
    }
    return render(request,'blog/contact.html',context)

def all_blogs(request,cid=0):
    #blogs=Blog.objects.all()
    if cid==0:
        blogs=Blog.objects.filter(publish=True).order_by('-update_at')
    else:
        blogs=Blog.objects.filter(publish=True,category=cid).order_by('-update_at')
    categories= BlogCategory.objects.all().order_by('category')
    context={
        'blogs':blogs,
        'categories':categories
    }
    return render(request,'blog/blog.html',context)

def blog_details(request, bid):
    blog = get_object_or_404(Blog, pk=bid)
    comment = Comment.objects.filter(blog=blog).order_by('-created_at')
    #blog=Blog.objects.filter(id=bid)
    context={
        'blog':blog,
        'comments':comment
    }
    return render(request,'blog/details.html',context)

def comment(request):
    if request.method=="POST":
        user=request.user
        blog_id = request.POST.get('bid')
        comment = request.POST.get('comment')

        blog = Blog.objects.get(id=blog_id)

        comment = Comment(user=user,blog=blog,comment=comment)
        comment.save()

        return redirect('/blog/'+blog_id)


# def blog_details(request, bid):
#     blog = get_object_or_404(Blog, pk=bid)
#     comments = blog.comments.all()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = blog
#             comment.author = request.user
#             comment.save()
#             return render(request,'blog/details.html')
#     else:
#         form = CommentForm()

#     context = {
#         'blog': blog,
#         'comments': comments,
#         'form': form,
#     }
#     return render(request, 'blog/details.html', context)

# def blog_details(request, bid):
#     blog = get_object_or_404(Blog, pk=bid)
#     comments = blog.comments.all()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = blog
#             comment.author = request.user
    #         comment.save()
    #         #return redirect('blog_details', bid=blog.pk)
    #         return render(request, 'blog/details.html', context)
    # else:
    #     form = CommentForm()

    # context = {
    #     'blog': blog,
    #     'comments': comments,
    #     'form': form,
    # }
    # return render(request, 'blog/details.html', context)





