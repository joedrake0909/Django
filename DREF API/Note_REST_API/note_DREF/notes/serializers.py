from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    
    title = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
    )
    
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)


    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'user']


