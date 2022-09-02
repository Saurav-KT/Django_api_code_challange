from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import EmpDetails
from django.http.response import Http404


class EmployeeDetailsViews(APIView):

    def get(self, request, EMP_ID=None):
        try:
            if EMP_ID:
                item = EmpDetails.objects.get(EMP_ID=EMP_ID)
                serializer = EmployeeSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            items = EmpDetails.objects.all()
            serializer = EmployeeSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        except EmpDetails.DoesNotExist:
            raise Http404

    def put(self, request, EMP_ID=None, format=None):
        try:
            emp_update = EmpDetails.objects.get_or_create(EMP_ID=EMP_ID)[0]
            if emp_update:
                serializer = EmployeeSerializer(instance=emp_update, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"status": "error", "data": "Record does not exist "}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, EMP_ID, format=None):
        item = get_object_or_404(EmpDetails, EMP_ID=EMP_ID)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
