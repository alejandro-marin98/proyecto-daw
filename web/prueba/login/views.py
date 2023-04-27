from django.shortcuts import render, redirect
from .forms import RegisterForm, FormularioLogin
from django.contrib.auth import login, logout
from .models import User
from solicitudes.views import isFriendOf, getFriendListsByUsername
from gestionLibros.views import getLibrosByUsername
from .models import User


def getAllUsers():
    return list(User.objects.all().exclude(is_superuser=True))


def createUser(request):

    if (request.method == 'GET'):
        return render(request, 'register.html', {'form': RegisterForm()})

    form = RegisterForm(data=request.POST)
    
    if form.is_valid():
        user = User(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            biografia=request.POST['biografia'],
        )
        user.save()
        login(request, user)
        return redirect('/')

    else:
        return render(request, 'register.html', {'form': form})


def loginUser(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {'form': FormularioLogin()}
                      )

    form = FormularioLogin(data=request.POST)

    if form.is_valid():
        usrnm = request.POST.get('username')
        pw = request.POST.get('password')
        user = User.objects.filter(username=usrnm, password=pw)[0]
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html', {'form': form})


def cerrarSesion(request):
    logout(request)
    return redirect('/')


def profile(request):
    username = request.POST.get('username')

    if not request.user.is_authenticated and not username:
        return redirect('/login')

    if request.user.is_authenticated and not username:
        libros = getLibrosByUsername(request.user.username)
        fecha = request.user.date_joined
        fecha_esp = fecha.strftime('%d-%m-%Y')
        return render(request, 'miPerfil.html', {'usu': request.user, 'libros': libros, 'mostrar': True,
                                                 'fecha_union': fecha_esp})

    match = User.objects.filter(username=username)[0]
    fecha = match.date_joined
    fecha_esp = fecha.strftime('%d-%m-%Y')

    if (not request.user.is_authenticated) and username:
        match = User.objects.filter(username=username)[0]
        return render(request, 'miPerfil.html', {'usu': match, 'fecha_union': fecha_esp})

    match = User.objects.filter(username=username)[0]
    libros = getLibrosByUsername(match.username)
    if match == request.user:
        return render(request, 'miPerfil.html', {'usu': match, 'libros': libros, 'mostrar': True,
                                                 'fecha_union': fecha_esp})

    estado = isFriendOf(username, request.user.username)

    if estado:
        return render(request, 'miPerfil.html', {'usu': match, 'libros': libros,  'mostrar': True, 'fecha_union': fecha_esp})

    return render(request, 'miPerfil.html', {'usu': match, 'libros': libros, 'input': True, 'fecha_union': fecha_esp})


def friends(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    def getFriendsAndNotFriendList():
        accepted, pending = getFriendListsByUsername(request.user.username)

        all_users = getAllUsers()

        all_users.remove(request.user)

        def filter_user(user):
            return user.username not in [
                i['usuario'] for i in accepted
            ]

        not_friend_users = list(filter(filter_user, all_users))

        pending_users_names = [i['usuario'] for i in pending]

        def filter_status_request(user): return [
            user, 'PENDIENTE'] if user.username in pending_users_names else [user, 'NO_PENDIENTE']

        filtered_not_friends_list = list(
            map(filter_status_request, not_friend_users))

        return accepted, filtered_not_friends_list

    retrieved_friends, not_friends = getFriendsAndNotFriendList()

    return render(request, 'misAmigos.html', {'amigos': retrieved_friends, 'no_amigos': not_friends})
