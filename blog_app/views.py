from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog_app/blog_post_list.html',{})
