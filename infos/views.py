from django.shortcuts import render
from django.http import HttpResponse

def show_main_page(request):
	c = {
      	"title": "Main Page"
       }
	return render(
    	    request=request,
    	    template_name="infos/main.html",
    	    context=c
	)


def show_about_me_page(request):
	c = {
        "title": "About Me"
        }
	return render(
    	    request=request,
    	    template_name="infos/aboutme.html",
    	    context=c
	)


def show_contact_page(request):
	c = {
      	"title": "Contact"
     	}
	return render(
    	    request=request,
    	    template_name="infos/contact.html",
    	    context=c
	)