from rest_framework import serializers  
from notes_api.models import NotesModel  
  
  
class NotesSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = NotesModel  
        fields = "__all__"