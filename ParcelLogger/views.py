# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from ParcelLogger.models import Student
from ParcelLogger.common import findStudentFromBox

def index(request):
    pageTemplate = loader.get_template('ParcelLogger/index.html')
    pageContext = Context({})
    return render_to_response('ParcelLogger/index.html', 
                              {}, 
                              context_instance=RequestContext(request))

def submit(request):
    
    boxStudent = findStudentFromBox(int(request.POST['boxId']))

    return render_to_response('ParcelLogger/submit.html', 
                              {'herp': boxStudent}, 
                              context_instance=RequestContext(request))