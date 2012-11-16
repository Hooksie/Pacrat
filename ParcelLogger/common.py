# Commonly used functions

from ParcelLogger.models import Student

def findStudentFromBox(boxNumber):
    return Student.objects.filter(postbox__boxNumber__exact=boxNumber)