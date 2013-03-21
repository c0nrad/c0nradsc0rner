# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category
from django.core.mail import send_mail
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.order_by('-posted')[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def aboutme(request):
    return render_to_response('aboutme.html', { })

def contactMe(request):
    p = request.POST

    if p.has_key("message"):
        message = p["message"]
        name = "Anonymous" if not p.has_key("name") else p["name"]
        email = "poptarts4" if not p.has_key("email") else p["email"]
        message = "\nName: " + name + "\nEmail: " + email + "\n" + message

        send_mail('c0nradsc0rner: Contact!', message , "poptarts4liffe@gmail.com", 
                  ['poptarts4liffe@gmail.com'], fail_silently=False)

        c = {}
        c.update(csrf(request))
        return render_to_response('contactMe.html', context_instance=RequestContext(request))
    else:
        return render_to_response('contactMe.html', {})