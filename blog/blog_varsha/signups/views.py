from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

from signups.forms import SignUpForm

def home(request):

	form = SignUpForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request,'Congrulation for your joining')
		return HttpResponseRedirect('/thank-you/')
	
	return render_to_response("templates/signups.html",
                               locals(),
                               context_instance = RequestContext(request))



def thankyou(request):
	
	return render_to_response("templates/thankyou.html",
                               locals(),
                               context_instance = RequestContext(request))