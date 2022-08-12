from config.wsgi import *

from core.erp.models import Type, Employee
# Create your tests here.

#Listar
# query = Type.objects.all()
# print(query)
#
# #insercion
# t = Type(name='Accionista').save()

#Editar
# try:
#     t = Type.objects.get(pk=4)
#     t.name = 'Chanchito feliz'
#     t.save()
# except Exception as e:
#     print(e)


#ELIMINAr
# t = Type.objects.get(pk=4)
# t.delete()


#obj =Type.objects.filter(name__icontains='chan') #contiene
#obj = Type.objects.filter(name__startswith='a')# empiezan
#obj = Type.objects.filter(name__endswith='z')# terminan
#obj = Type.objects.filter(name__in=['Presidente', 'Acionista Leon']).count()# lo mismo de la BD
#obj = Type.objects.filter(name__contains=['Pre']).query# query para hacer en la BD
#obj = Type.objects.filter(name__endswith='e').exclude(id=3)#excluye terminados en e

# obj = Employee.objects.filter(type_id=1)
#
# for i in Type.objects.filter(employee__dni=1):#excluye terminados en e con iteracioon
#     print(i.name)
#


#for i in Type.objects.filter(name__endswith='e')[:1]:#excluye terminados en e con iteracioon
    #print(i.name)