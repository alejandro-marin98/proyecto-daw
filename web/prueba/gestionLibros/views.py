from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Libros, Listas, Opiniones
from django.http import HttpResponse
import time
def getLibrosByUsername(username):
    try:
        return Listas.objects.all().select_related('user', 'book').filter(user=username).exclude(estado='sin_guardar')
    except:
        return []

def getOpinionesByIsbn(isbn):
    try:
        opiniones = Opiniones.objects.all().select_related('user', 'book').filter(book=isbn)
        return opiniones
    except:
        return []

def getOpinionesByUser(username):
    opiniones = Opiniones.objects.all().select_related('user', 'book').filter(user=username)
    return opiniones

def getBookState(username, isbn):
    match = list(Listas.objects.filter(user=username, book=isbn))
    return False if len(match) == 0 else match[0]

def getBookByCoincidence(condition):
    # La i es para que no tenga en cuenta minusculas y mayusculas
    q1 = Libros.objects.filter(isbn__icontains=condition)
    q2 = Libros.objects.filter(titulo__icontains=condition)
    rs = set(list(q1) +  list(q2))

    return list(rs)

def getAllBooks():
    return list(Libros.objects.all())

def showBooks(request):
    return render(request, 'libros.html')


def getBooks(_request):
    time.sleep(1)
    libros = list(Libros.objects.values())
    data = {'libros': libros}
    return JsonResponse(data)


def showBookDetailsByIsbn(request, isbn):
    libro = Libros.objects.filter(isbn=isbn)
    
    if not libro[0]:
        return HttpResponse('Mal')

    opiniones = getOpinionesByIsbn(isbn)

    if request.user.is_authenticated:
        username = request.user.username
        estado = getBookState(username, isbn)
        if not estado:
            return render(request, 'paginaLibro.html', {'libro': libro[0], 'estado': 'sin_guardar', 'opiniones': opiniones})
        
        return render(request, 'paginaLibro.html', {'libro': libro[0], 'estado': estado.estado, 'opiniones': opiniones})

    return render(request, 'paginaLibro.html', {'libro': libro[0], 'opiniones': opiniones})


def setLista(request=None, operation='', username='', isbn=''):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        username = request.POST.get('username')
        isbn = request.POST.get('isbn')
        if not operation or not username or not isbn:
            return redirect('/')

        if operation not in ('pendiente', 'leyendo', 'leido', 'sin_guardar'):
            return redirect(f'/libros/getBooks/{isbn}')

        result = getBookState(username, isbn)

        if not result:
            query = Listas.objects.create(
                estado=operation, 
                user=request.user, 
                book=Libros.objects.get(isbn=isbn))
            query.save()
            return redirect(f'/libros/getBooks/{isbn}')

        if result.estado == operation:
            return redirect(f'/libros/getBooks/{isbn}')
        
        result.estado = operation

        result.save()

        return redirect(f'/libros/getBooks/{isbn}')

    else:
        return HttpResponse('No va por POST')

def addOpinion(request=None, opinion='', username='', isbn=''):
    if not request.method == 'POST':
        return HttpResponse('No va por POST')
    
    ruta_anterior = ''
    splited = [str(x) for x in request.META["HTTP_REFERER"].split('/')[3:-1]]
        
    for split in splited:
        ruta_anterior += '/' + str(split)

    opinion = request.POST.get('opinion')
    username = request.POST.get('username')
    isbn = request.POST.get('isbn')

    if not opinion or not username or not isbn:
       
        return redirect(ruta_anterior)

    query = Opiniones.objects.create(
        opinion=opinion, 
        user=request.user, 
        book= Libros.objects.get(isbn=isbn))
    query.save()

    return redirect(f'/libros/getBooks/{isbn}')

def misLibros(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    username = request.user.username
    libros = getLibrosByUsername(username)

    return render(request, 'misLibros.html', {'res': libros})

def searchBook(request):
    if not request.method == 'POST':

        return redirect('/libros')
        
    condition = request.POST.get('condition')

    libros = getBookByCoincidence(condition=condition)
    return render(request, 'buscarLibro.html', {'matches': libros})
