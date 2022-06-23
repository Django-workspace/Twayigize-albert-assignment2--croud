from django.urls import path
from .import views



urlpatterns = [
    path("create", views.createTrainees, name="create"),
    path("listtrainees", views.listAllTrainees, name= "lisTrainees"),
    path("edittrainees/<int:id>", views.editTrainees,name= "edittraineers"),
    path("updatetrainees/<int:id>", views.updateTrainees, name= "updatetrainees"),
    path('delete/<int:id>', views.deleteTraineer, name="seletetrainees"),
    path("login", views.login, name="login")

]