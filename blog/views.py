# Create your views here.
from blog.models import Post, Thought
from django.shortcuts import render_to_response


def tagpage(request,tag):
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response("tagpage.html",{"posts":posts,"tag":tag})


def myresume(request):
	return render_to_response("myresume.html")

def homepage(request):
	thoughts = Thought.objects.all()
	return render_to_response("homepage.html",{"thoughts":thoughts})





	