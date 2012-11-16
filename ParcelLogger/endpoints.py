from django.http import HttpResponse
from ParcelLogger.common import findStudentFromBox

def findStudent(request):
    
    if len(request.POST):
        student = findStudentFromBox(int(request.POST['boxId']))
        if len(student):
            response = {'firstName': student[0].firstName,
                        'lastName': student[0].lastName}
        else:
            response = {'firstName': '',
                        'lastName': ''}
        
    else:
        response = HttpResponse()
        response.status_code = 200
        
    return response