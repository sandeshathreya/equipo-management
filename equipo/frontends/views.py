from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.template.loader import get_template
from django.template import Context
from django.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth 
from django.http import HttpResponseRedirect
from frontends.forms import LoginForm






def lists(request):
    log="login.png"
    l={'picture':log}
    return render_to_response('/home/aditya/Desktop/finally/equipo/file/templates/success.html',l,RequestContext(request))
	

def login1(request):
    log="login.png"
    l={'picture':log}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/login.html',l,RequestContext(request))

def fandr(request):
    log="login.png"
    l={'picture':log}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/faqandreference.html',l,RequestContext(request))

def refsec(request):
    log="login.png"
    l={'picture':log}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/referencesection.html',l,RequestContext(request))
      
   

def hodlogin(request):
	if request.user.is_authenticated():
                return HttpResponseRedirect('hodnewdash.html')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
			authid	 = form.cleaned_data['AuthID']
			if authid==1234:
                        	hod = authenticate(username=username, password=password)
                        	if hod is not None:
                                	login(request, hod)
                                	return HttpResponseRedirect('hodnewdash.html')
                        	else:
                                	return render_to_response('hodlogin.html', {'form': form}, context_instance=RequestContext(request))
			else:
				return render_to_response('hodlogin.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('hodlogin.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('hodlogin.html', context, context_instance=RequestContext(request))

def guidelogin(request):
	if request.user.is_authenticated():
                return HttpResponseRedirect('guidenewdash.html')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
			authid	 = form.cleaned_data['AuthID']
			if authid==3456:
                        	guide = authenticate(username=username, password=password)
                        	if guide is not None:
                                	login(request, guide)
                                	return HttpResponseRedirect('guidenewdash.html')
                        	else:
                                	return render_to_response('guidelogin.html', {'form': form}, context_instance=RequestContext(request))
			else:
				return render_to_response('guidelogin.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('guidelogin.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('guidelogin.html', context, context_instance=RequestContext(request))

def teamlogin(request):
	if request.user.is_authenticated():
                return HttpResponseRedirect('teamnewdash.html')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
			authid	 = form.cleaned_data['AuthID']
			if authid==6789:
                        	team = authenticate(username=username, password=password)
                        	if team is not None:
                                	login(request, team)
                                	return HttpResponseRedirect('teamnewdash.html')
                        	else:
                                	return render_to_response('teamlogin.html', {'form': form}, context_instance=RequestContext(request))
			else:
				return render_to_response('teamlogin.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('teamlogin.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('teamlogin.html', context, context_instance=RequestContext(request))






    

def hoddashboard(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/hodnewdash.html',t,RequestContext(request))
            

def banner(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/banner.html',t,RequestContext(request))

def options2(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/options2.html',t,RequestContext(request))

def hodeval(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/makeevaluation.html',t,RequestContext(request))

def viewsynopsis(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/viewsynopsis.html',t,RequestContext(request))

def guidenewdash(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/guidenewdash.html',t,RequestContext(request))

def options1(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/options1.html',t,RequestContext(request))

def something(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/something.html',t,RequestContext(request))

def teamnewdash(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/teamnewdash.html',t,RequestContext(request))

def options(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/options.html',t,RequestContext(request))

def synopsis(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/synopsis.html',t,RequestContext(request))

def viewgrades(request):
    team="team.png"
    t={'team1':team}
    return render_to_response('/home/aditya/Desktop/finally/equipo/frontends/templates/viewgrades.html',t,RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect("/")




