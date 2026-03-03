from rest_framework import viewsets, status
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        print("Performing create operation for Note")

        print(f'Self:{self}')
        print(f'Self.queryset: {self.queryset}')

        print(f'Serializer: {serializer}')
        print(f'Serializer.class: {serializer.__class__.__name__}')

        print(f'Data being saved: {serializer.validated_data}')

        if 'title' in serializer.validated_data:
            title = serializer.validated_data['title']
            print(f'Title being saved: {title}')
        else:
            print('No title provided in validated data.')
        
        if 'content' in serializer.validated_data:
            content = serializer.validated_data['content']
            print(f'Content being saved: {content}')
        else:
            print('No content provided in validated data.')

    
        serializer.save()

        print("Note created successfully.")
    


    def retrieve(self, request, pk=None):
        try:
            note = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(note)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response(
                {"error": f'Note with id {pk} not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

