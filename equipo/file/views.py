from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from equipo.file.models import Document
from equipo.file.forms import docform

def enterfile(request):
	if request.method=='POST':
		form=docform(request.POST,request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
                        newdoc.save()
			return HttpResponseRedirect('success.html')
		else:
			form=docform()
			return render_to_response(
               '/home/aditya/Desktop/finally/equipo/file/templates/uploadfile.html',{'form':form},                		                         context_instance=RequestContext(request))
	else:
		form=docform()
		return render_to_response(
               '/home/aditya/Desktop/finally/equipo/file/templates/uploadfile.html',{'form':form},                		                         context_instance=RequestContext(request))
		
def success(request):
	log="login.png"
        l={'picture':log}
        return render_to_response('/home/aditya/Desktop/finally/equipo/file/templates/success.html',l,RequestContext(request))
	

def uploads(request):
	
	documents=Document.objects.all()
	return render_to_response(
        '/home/aditya/Desktop/finally/equipo/file/templates/uploads.html',
        {'documents': documents},
        context_instance=RequestContext(request)
        )			