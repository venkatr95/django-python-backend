from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from notes_api.models import NotesModel
from notes_api.serializers import NotesSerializer
import math
from datetime import datetime


class Notes(generics.GenericAPIView):
    serializer_class = NotesSerializer
    queryset = NotesModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        notes = NotesModel.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response(
            {
                "status": "success",
                "total": total_notes,
                "page": page_num,
                "last_page": math.ceil(total_notes / limit_num),
                "notes": serializer.data,
            }
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "note": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": "fail", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class NotesDetail(generics.GenericAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer

    def get_task(self, pk):
        try:
            return NotesModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        task = self.get_task(pk=pk)
        if task is None:
            return Response(
                {"status": "fail", "message": f"Task with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(task)
        return Response({"status": "success", "note": serializer.data})

    def delete(self, request, pk):
        task = self.get_task(pk)
        if task is None:
            return Response(
                {"status": "fail", "message": f"Task with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)