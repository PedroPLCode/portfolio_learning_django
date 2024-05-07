from django.shortcuts import render
from django.http import HttpResponse

def show_main_page(request):
	c = {
      	"title": "main page"
       }
	return render(
    	    request=request,
    	    template_name="infos/main.html",
    	    context=c
	)


def show_about_me(request):
	c = {
        "title": "about me"
        }
	return render(
    	    request=request,
    	    template_name="infos/aboutme.html",
    	    context=c
	)


def show_contact(request):
	c = {
      	"title": "contact"
     	}
	return render(
    	    request=request,
    	    template_name="infos/contact.html",
    	    context=c
	)