from django.shortcuts import render, redirect
from .models import Solicitudes
from login.models import User
from django.http import JsonResponse, HttpResponse
import json
from gestionLibros.models import Libros

def getSolicitudes(request=None, username=''):
    data = None
    try:
        listaSolicitudes = list(Solicitudes.objects.filter(usr_recibe=username, estado='PENDIENTE'))
        data = {'cantSolicitudes': len(listaSolicitudes)}
    except:
        data = {'cantSolicitudes': 0}
    return HttpResponse(json.dumps(data))

def isSolicitudValid(sender, destinatary):
    sol = Solicitudes.objects.filter(usr_envia_id=sender, usr_recibe_id=destinatary, estado='ACEPTADA')
    sol2 = Solicitudes.objects.filter(usr_envia_id=destinatary, usr_recibe_id=sender, estado='ACEPTADA')
    return len(sol) == 0 and len(sol2) == 0

def isFriendOf(usr_1, usr_2):
    res = Solicitudes.objects.filter(usr_recibe_id=usr_2, usr_envia_id=usr_1, estado='ACEPTADA')
    res2 = Solicitudes.objects.filter(usr_recibe_id=usr_1, usr_envia_id=usr_2, estado='ACEPTADA')
    return False if len(res) == 0  and len(res2) == 0 else True

def getSolicitudesByUsername(username):
    solicitudes = Solicitudes.objects.filter(usr_recibe=username, estado='PENDIENTE')
    ok = []

    for sol in solicitudes:
        if sol.usr_envia == username:
            ok.append(
                {
                    'usuario': sol.usr_recibe,
                    'id': sol.id_solicitud
                }
            )
        else:
            ok.append(
                {
                    'usuario': sol.usr_envia,
                    'id': sol.id_solicitud
                }
            )
    
    return ok

# def getFriendsListByUsername(username):
#     accepted = Solicitudes.objects.all().select_related('usr_recibe').filter(usr_recibe=username).filter(estado='ACEPTADA')
#     return list(opiniones)

def getFriendListsByUsername(username):
    matches = Solicitudes.objects.all().select_related('usr_recibe').filter(usr_envia=username)
    accepted = matches.filter(estado='ACEPTADA')
    pending = matches.filter(estado='PENDIENTE')

    matches2 = Solicitudes.objects.all().select_related('usr_envia').filter(usr_recibe=username)
    accepted2 = matches2.filter(estado='ACEPTADA')
    pending2 = matches2.filter(estado='PENDIENTE')

    full_accepted = list(accepted) + list(accepted2)

    aceptadas_bien = []

    for sol in full_accepted:
        if sol.usr_envia.username == username:
            aceptadas_bien.append(
                {'usuario': sol.usr_recibe.username,'estado': sol.estado, 'id_solicitud': sol.id_solicitud}
            )
        else:
            aceptadas_bien.append(
                {'usuario': sol.usr_envia.username,'estado': sol.estado, 'id_solicitud': sol.id_solicitud}
            )

    full_pending = list(pending) + list(pending2)
    pendientes_bien = []

    for sol in full_pending:
        if sol.usr_envia.username == username:
            pendientes_bien.append(
                {'usuario': sol.usr_recibe.username,'estado': sol.estado}
            )
        else:
            pendientes_bien.append(
                {'usuario': sol.usr_envia.username,'estado': sol.estado}
            )

    return aceptadas_bien, pendientes_bien 

def showSolicitudes(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    sol = getSolicitudesByUsername(request.user.username)
    return render(request, 'solicitudes.html', {'solicitudes': sol})

def responder(request):
    ruta_anterior = '/' + str([str(x) for x in request.META["HTTP_REFERER"].split('/')[3:]][0])

    if not request.method == 'POST':
        return redirect('/')

    if not request.user.is_authenticated:
        return redirect('/')
    
    respuesta = request.POST.get('respuesta')
    id_solicitud = request.POST.get('id_solicitud')
    

    if not respuesta or not id_solicitud:
        return redirect('/')
    
    if respuesta not in ['aceptar', 'rechazar']:
        return redirect('/')

    try:
        sol = Solicitudes.objects.get(id_solicitud=id_solicitud)
        if respuesta == 'aceptar':
            sol.estado = 'ACEPTADA'
        else:
            sol.estado = "RECHAZADA"
        sol.save()
        return redirect(ruta_anterior)
    except:
        return redirect(ruta_anterior)
    
def mandar_solicitud(request):
    # if not request.user.is_authenticated or not request.method == 'POST':
    #     return redirect('/')
    
    sender = request.POST.get('usr_env')
    destinatary = request.POST.get('usr_rec')
    ruta_anterior = '/' + str([str(x) for x in request.META["HTTP_REFERER"].split('/')[3:]][0])

    if isSolicitudValid(sender, destinatary):
        sol = Solicitudes.objects.create(usr_envia_id=sender, usr_recibe_id=destinatary, estado='PENDIENTE')
        sol.save()
        return redirect(ruta_anterior) 

    return redirect(ruta_anterior) 

