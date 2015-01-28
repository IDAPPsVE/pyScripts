import requests
import json
import time
import os

headers = {'content-type': 'application/json'}
dominio = "http://104.131.92.103:5858"

b =  requests.post(dominio + '/MaraBox/api/boxid', data=json.dumps({}), headers=headers)
bid = b.json()
boxid = bid['box']['_id']
print boxid
ba =  requests.post(dominio + '/MaraBox/api/boxadminid', data=json.dumps({'boxid':boxid}), headers=headers)
bai = ba.json()
boxadminid = bai['box']['IDAPP']['Codigo']
print boxadminid

"""
print
print "Boxid y BoxAdminid obtenidos"
print
print "Guardando App propietario superusuario"
print
for i in range(1):
    url = dominio + '/signup'
    payload = {'email': 'su@su.com','password': '123456','contrato':1}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

print
print "Guardando APP admin"
print
for i in range(4):
    url = dominio + '/MaraBox/signup'
    payload = {'cedula': '123456'+str(i),'email': 'appadmin'+str(i)+'@e.com', 'idBoxAdmin':boxadminid,'tipo':5,'password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
"""

print
print "Guardando App entrenador"
print
for i in range(4):
    url = dominio + '/MaraBox/signup'
    payload = {'cedula': '987654'+str(i),'email': 'entrenador'+str(i)+'@e.com', 'idBoxAdmin':boxadminid,'tipo':6,'password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

"""
print
print "Guardando usuario de la app"
print
for i in range(500):
    url = dominio + '/MaraBox/api/signup'
    payload = {'cedula': '123456789'+str(i),'email': 'a'+str(i)+'@a.com', 'idBoxCode':'hkbbiLu6','password': '123456'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    

print
print "Guardando info de usuario"
print
for i in range(500):
    url = dominio + '/MaraBox/registroInfoUsuario'
    payload = {'nombres': 'name'+str(i),'apellidos': 'apellido'+str(i), 'ciudad':'Maracaibo','estado': 'Zulia',
    'telefono':'04245847883', 'fechaNacimiento':'30-03-1989'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

print
print "Guardando notificaciones"
print
for i in range(48):
    url = dominio + '/MaraBox/admin/nuevaNotificacion'
    payload = {'titulo': 'titulo'+str(i),'Mensaje': 'Este es el mensaje numero '+str(i)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

print
print "Guardando Dias de Descancio"
print
for i in range(20):
    url = dominio + '/MaraBox/admin/registroFeriado'
    payload = {'fecha': str(i)+'-06-2015','diaCompleto': 1, 'hora':'', 'motivo':'No me dio la gana de abrir'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

print
print "Guardando Solvencia"
print
for i in range(500):
    url = dominio + '/MaraBox/api/solvencia'
    payload = {'cedula': '123456789'+str(i),'fechaInicio': '01-01-2015', 'fechaCulminacion':'31-12-2015'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    time.sleep(1)




print
print
'/MaraBox/admin/nuevoWod'
dictWU = [{idEjercicio : req.body.buyout[k], Cantidad    : req.body.cbo[k]}]
wod.MaraBox.Nombre = req.body.nombreWOD;
wod.MaraBox.Timecap = req.body.timecap;
wod.MaraBox.idBox = h.getMaraBoxId();
wod.MaraBox.WarmUp = dictWU;
wod.MaraBox.WOD = dictWD;
wod.MaraBox.BuyOut = dictBO;
wod.MaraBox.Fecha = moment(moment().format('YYYY-MM-DD'));


print
print
'/MaraBox/admin/nuevaEvento'
e.MaraBox.Imagen = i;
e.MaraBox.Nombre = n;
e.MaraBox.Ciudad = c;
e.MaraBox.Estado = es;
e.MaraBox.Direccion = d;
e.MaraBox.FechaInicio = fi;
e.MaraBox.FechaCulminacion = fc;
e.MaraBox.Costo = cos;
"""