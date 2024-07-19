from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializer import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# Get and Post
def accounts(request):


    if request.method == "GET":
        info = Account.objects.all()
        account_serializer = AccountSerializer(info, context={'request':request}, many=True)
        return Response(account_serializer.data)
    
    if request.method == "POST":
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_account(request, id):
    try:
        account = Account.objects.get(pk=id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountView(APIView):
    serializer_class = AccountSerializer
    
    def get(self, request):
        output = [
            {"id": output.id, "Name": output.name, "Email": output.email, "Password": output.password}
                for output in Account.objects.all()
                ]
        return Response(output)
    
    def getSingle(self, request):
        
        item = Account.objects.get(pk=request.GET['pk'])
        output = {"Name": item.name, "Email": item.email, "Password": item.password}
        return Response(output)
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request):
        print(request)
        todel = Account.objects.get(pk=request.data.get("id"))
        todel.delete()
        return Response(request)