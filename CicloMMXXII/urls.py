from django.urls import path
from CicloMMXXII import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('cursos', views.cursos,   name="cursos"),
  path('alta_curso', views.curso_form),
  path('search_cursos', views.search_cursos),
  path('delete_curso/<int:id>', views.delete_curso, name="delete_curso"),
  path('edit_curso/<int:id>', views.edit_curso, name="edit_curso"),
  path('edit_curso/', views.edit_curso, name="edit_curso"),
  path("cadetes", views.cadetes, name="cadetes"),
  path("alta_cadetes", views.alta_cadetes, name="alta_cadetes"),
  path('search_cadete', views.search_cursos),
  path('delete_cadetes/<int:id>', views.delete_cadetes, name="delete_cadetes"),
  path('edit_cadete/<int:id>', views.edit_cadete, name="edit_cadete"),
  path('edit_cadete/', views.edit_cadete, name="edit_cadete"),
  path("instructors", views.instructors, name="instructors"),
  path("alta_instructors", views.alta_instructors),
  path('search_instructors', views.search_instructors, name="search_instructors"),
  path('delete_instructors/<int:id>', views.delete_instructors, name="delete_instructors"),
  path('edit_instructors/<int:id>', views.edit_instructors, name="edit_instructors"),
  path('edit_instructors/', views.edit_instructors, name="edit_instructors"),
  path("login", views.login_request, name="login"),
  path('logout', LogoutView.as_view(template_name="logout.html"),name="Logout"),
  path("contact", views.contact, name="contact"),
  path("about",   views.about,   name="about"),
  path("subjects", views.subjects, name="subjects"),
  path("messages", views.messages, name="messages"),
  path("edit_profile", views.edit_profile, name="edit_profile"),
  path("search", views.search),
  path("register", views.register, name="register")
  
  
]