from django.urls import path  
from notes_api.views import Notes, NotesDetail  
  
urlpatterns = [path("", Notes.as_view()),   
               path("<str:pk>", NotesDetail.as_view())]
