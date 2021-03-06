from django.db import models

class Student(models.Model):
    studentId = models.IntegerField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    #fwdAdddr = models.ForeignKey(FwdAddress)
    
    def __str__ (self):
        return self.getFullName()
    
    def getFullName(self):
        return self.firstName + " " + self.lastName
    
    
class Package(models.Model):
    studentId = models.ForeignKey(Student)
    dateReceived = models.DateField(auto_now_add=True)
    datePickedUp = models.DateTimeField()
    
class Postbox(models.Model):
    StatusOpen = "opn"
    StatusAssigned = "ass"
    StatusBroken = "brk"
    StatusPending = "pnd"
    validStatuses = (
                     (StatusOpen, 'Open'), 
                     (StatusAssigned, 'Assigned'),
                     (StatusBroken, 'Broken'),
                     (StatusPending, 'Pending'),
                    )
    
    status = models.CharField(max_length=3, choices=validStatuses, default=StatusOpen)
    
    boxNumber = models.IntegerField()
    owner = models.ForeignKey(Student)
    
#class FwdAddress(models.Model):
    