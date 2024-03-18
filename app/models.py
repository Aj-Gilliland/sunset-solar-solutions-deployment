from django.db import models

class ConApp(models.Model):
        name = models.CharField(max_length=200, null=False, blank=False) 
        email = models.CharField(max_length=200, null=False, blank=False) 
        note = models.CharField(max_length=200, null=False, blank=False) 
        def __str__(self):
                return self.name
        
def delete_ConApp(id):
    entry = ConApp.objects.get(id=id)
    entry.delete()
    return entry

def create_ConApp(name, email, note):
    entry = ConApp(name=name, email=email, note=note)     
    entry.save()
    return entry

def all_ConApp():
    return ConApp.objects.all()

def find_id_by_name_con(name):
    person = ConApp.objects.get(name=name)
    return person.id


class EmpApp(models.Model):
        first_name = models.CharField(max_length=200, null=False, blank=False) 
        last_name = models.CharField(max_length=200, null=False, blank=False) 
        position = models.CharField(max_length=200, null=False, blank=False) 
        number = models.CharField(max_length=200, null=False, blank=False)
        email = models.CharField(max_length=200, null=False, blank=False)
        def __str__(self):
                return self.first_name
        
def delete_EmpApp(id):
    entry = EmpApp.objects.get(id=id)
    entry.delete()
    return entry

def create_EmpApp(first_name, last_name, position, number, email):
    entry = EmpApp(first_name=first_name, last_name=last_name, position=position, number=number, email=email)     
    entry.save()
    return entry

def all_EmpApp():
    return EmpApp.objects.all()

def find_id_by_name(first_name,last_name):
    person = EmpApp.objects.get(first_name=first_name, last_name=last_name)
    return person.id