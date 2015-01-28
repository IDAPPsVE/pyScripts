import requests
import json
import time
import os
headers = {'content-type': 'application/json'}
dominio = "http://104.131.92.103:5858"

print "Guardando Contactos"
for i in range(10):
    url = dominio + '/contacto'
    payload = {'nombre': 'Fulano','apellido': 'Sultano', 'email':'fulano@gmail.com','mensaje':'Mensaje de prueba'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print "Contacto" + str(i)

print "Guardando Contrato"
def contrato():
    url = dominio + '/admin/registroContrato'
    payload = {'contrato': 1,'android': 1, 'ios':1,'administrativo':1,'facturacion': 'Mensual','rif': 'V-18808627-2', 
    'empresa':'IDAPP','telefonoOficina':'04245847883','telefonoPersonal':'04245847883','direccion':'Urb. Monte Bello Conjunto residencia los roques, calle O, #3',
    'correo':'vjfs18d@gmail.com','app':'MaraBox'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print "Contrato 1"
    
    for i in range(49):
        v = i+2
        payload1 = {'contrato': v,'android': 1, 'ios':1,'administrativo':1,'facturacion': 'Mensual','rif': 'V-18808627-2', 
        'empresa':'IDAPP','telefonoOficina':'04245847883','telefonoPersonal':'04245847883','direccion':'Urb. Monte Bello Conjunto residencia los roques, calle O, #3',
        'correo':'vjfs18'+str(i)+'@gmail.com','app':'IDAPP'}
        r1 = requests.post(url, data=json.dumps(payload1), headers=headers)
        print "Contrato" + str(i)
        
contrato()

print "Guardando Icarus"
for i in range(1):
    url = dominio + '/ias/ss/signup'
    payload = {'email': 'vjfs18@gmail.com','password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print "Icarus" + str(i)

print "Guardando IDAPP Admin"
for i in range(2):
    url = dominio + '/ias/admin/signup'
    payload = {'email': 'admin'+str(i)+'@gmail.com','password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print "IDAPP Admin" + str(i)

print "Guardando IDAPP Empleado"
for i in range(10):
    url = dominio + '/ias/staff/signup'
    payload = {'email': 'staff'+str(i)+'@gmail.com','password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print "IDAPP Empleado" + str(i)
