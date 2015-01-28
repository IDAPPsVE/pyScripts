import requests
import json
import time
import os

headers = {'content-type': 'application/json'}
dominio = "http://104.131.92.103:5858"

"""
print
print "Guardando clase de Prueba"
print
def nuevaClase():
    url = dominio + '/MaraBox/api/nuevaClase'
    payload = {'fecha': '27-01-2015','hora': '06:00', 'cupo':20, 'entrenador':'54c80b8b672495ea7d044a79'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
nuevaClase()
      
print
print "Guardando clase de Relleno"
print
for i in range(259):
    url = dominio + '/MaraBox/api/nuevaClase'
    payload = {'fecha': '27-01-2015','hora': '07:00', 'cupo':20, 'entrenador':'54c80b8b672495ea7d044a79'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    time.sleep(1)
"""
print
print "Guardando Asistencia"
print
for i in range(260*16*20):
    url = dominio + '/MaraBox/api/clase'
    r = requests.post(url, data=json.dumps({}), headers=headers)
    url1 = dominio + '/MaraBox/api/asistencia/registrar'
    payload = {'cedula': '123456789'+str(i),'hora': '06:00'}
    r1 = requests.post(url1, data=json.dumps(payload), headers=headers)
    