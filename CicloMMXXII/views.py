import email
from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import render
from CicloMMXXII.models import Curso, Cadetes, Instructor, Avatar
from django.template import loader
from CicloMMXXII.forms import Curso_forms, Cadetes_forms, Instructor_forms, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

#INICIO
def inicio(request):
    return render(request, "index.html")

#ABOUT
def about(request):
    return render(request, "about.html")

#CURSOS

def cursos(request):
    return render(request, "cursos.html")

@login_required
def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    document = plantilla.render(dicc)
    return HttpResponse( document )



##ALTA_CURSO
def curso_form(request):
    if request.method == "POST":
        my_form = Curso_forms(request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
        curso = Curso( name=datos['name'] , section=datos['section'])
        curso.save()
        return render(request, "cursos.html")
    return render(request, "forms.html")    

def search_cursos(request):
    return render(request, "search_cursos.html")

###DELETE CURSO
def delete_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()
    return render(request, "cursos.html",{"cursos": curso})

####EDIT CURSO
def edit_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        my_form = Curso_forms( request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
            curso.name    = datos['name']
            curso.section = datos['section']
            curso.save()

            curso = Curso.objects.all()
            return render(request, "cursos.html", {"cursos": curso})
    else:
        my_form = Curso_forms(initial={'name': curso.name, "section":curso.section})

    return render( request, "edit_curso.html", {"my_form": my_form, "curso": curso})

#####SEARCH CURSOS

def search(request):

    if request.GET['name']:
        name    = request.GET['name']
        cursos = Curso.objects.filter(name__icontains = name)
        return render( request, "results_search.html", {"cursos": cursos} )
    else:
        return HttpResponse("Error")


#CADETES

def cadetes(request):
    return render(request, "cadetes.html")

@login_required
def cadetes(request):
    cadetes = Cadetes.objects.all()
    dicc = {"cadetes" : cadetes}
    plantilla = loader.get_template("cadetes.html")
    document = plantilla.render(dicc)
    return HttpResponse( document )


##ALTA CADETES

def alta_cadetes(request):
    if request.method == "POST":
        my_form = Cadetes_forms(request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
            cadete = Cadetes( name=datos['name'] , lastname=datos['lastname'], email=datos['email'])
            cadete.save()
            return render(request, "forms.html")
    return render(request, "alta_cadetes.html")    

###DELETE CADETE
def delete_cadetes(request, id):
    cadete = Cadetes.objects.get(id=id)
    cadete.delete()

    cadete = Cadetes.objects.all()
    return render(request, "cadetes.html",{"cadetes": cadete})

####EDIT CADETE
def edit_cadete(request, id):
    cadete = Cadetes.objects.get(id=id)

    if request.method == "POST":

        my_form = Cadetes_forms( request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
            cadete.name     = datos['name']
            cadete.lastname = datos['lastname']
            cadete.email    = datos['email']
            cadete.save()

            cadete = Cadetes.objects.all()
            return render(request, "cadetes.html", {"cadetes": cadete})
    else:
        my_form = Cadetes_forms(initial={'name': cadete.name, "lastname": cadete.lastname, 'email': cadete.email})

    return render( request, "edit_cadete.html", {"my_form": my_form, "cadete": cadete})

#CONTACT
def contact(request):
    return render(request, "contact.html")

#SUBJECTS
@login_required
def subjects(request):
    return render(request, "subjects.html")

#MESSAGES
@login_required
def messages(request):
    return render(request, "messages.html")

#INSTRUCTORS
def instructors(request):
    return render(request, "instructors.html")

@login_required
def instructors(request):
    instructors = Instructor.objects.all()
    dicc = {"instructors" : instructors}
    plantilla = loader.get_template("instructors.html")
    document = plantilla.render(dicc)
    return HttpResponse( document )


##ALTA INSTRUCTORES

def alta_instructors(request):
    if request.method == "POST":
        my_form = Instructor_forms(request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
            instructor = Instructor( name=datos['name'], lastname=datos['lastname'], email=datos['email'], subject=datos['subject'])
            instructor.save()
            return render(request, "forms.html")
    return render(request, "alta_instructors.html")    

###DELETE INSTRUCTORS
def delete_instructors(request, id):
    instructor = Instructor.objects.get(id=id)
    instructor.delete()

    instructor = Instructor.objects.all()
    return render(request, "instructors.html",{"instructors": instructor})

#### EDIT INSTRUCTORS
def edit_instructors(request, id):
    instructor = Instructor.objects.get(id=id)

    if request.method == "POST":

        my_form = Instructor_forms( request.POST)
        if my_form.is_valid():
            datos = my_form.cleaned_data
            instructor.name    = datos['name']
            instructor.lastname = datos['lastname']
            instructor.email   = datos['email']
            instructor.subject = datos['subject']
            instructor.save()

            instructor = Instructor.objects.all()
            return render(request, "instructors.html", {"instructors": instructor})
    else:
        my_form = Instructor_forms(initial={'name': instructor.name, "lastname": instructor.lastname, 'email': instructor.email, 'subject': instructor.subject})

    return render( request, "edit_instructor.html", {"my_form": my_form, "instructor": instructor})

#####SEARCH INSTRUCTORS

def search_instructors(request):

    if request.GET['name']:
        name    = request.GET['name']
        cursos = Curso.objects.filter(name__icontains = name)
        return render( request, "results_search.html", {"instructors": instructors} )
    else:
        return HttpResponse("Error")


#CONTACT
def contact(request):
    return render(request, "contact.html")

#EDIT PROFILE

@login_required
def edit_profile(request):

    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            usuario.email = info['email']
            password = info['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "edit_profile.html", {"miFormulario":miFormulario, "usuario":usuario})


#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            usuario  = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            user = authenticate(username= usuario, password=passw)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "index.html",{"url":avatares[0].img.url})
                #return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            
            else:
                return HttpResponse(f"Usuario incorrecto")
        else:
            return HttpResponse(f"Incorrecto {form}")

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})    



# REGISTER

def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            
            form.save()
            return HttpResponse("User created")



    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})

