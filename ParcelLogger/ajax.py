from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from ParcelLogger.models import Student

@dajaxice_register
def FindStudent(request, boxNumber):
    
    boxStudent = Student.objects.filter(postbox__boxnumber__exact=int(boxNumber))
    ajaxResponse = Dajax()
    
    if boxStudent.len() == 0:
        pass # Some error here
    else:
        ajaxResponse.assign('#entry_firstName', 'value', 'hello')
        ajaxResponse.assign('#entry_lastName', 'value', 'world')
    
    return ajaxResponse.json()