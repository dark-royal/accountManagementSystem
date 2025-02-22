from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from account.models import Account
from account.serializers import AccountSerializers, AccountCreateSerializers


# Create your views here.
@api_view(['GET', 'POST'])
def list_accounts(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializers(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AccountCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


# def account_details(request,pk):
#     try:
#         account = Account.objects.get(pk=pk)
#         serializer = AccountSerializers(account)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     except Account.DoesNotExist:
#         return Response({"message": "Account not found"},status=status.HTTP_404_NOT_FOUND)
#
#
@api_view()
def account_details(request, pk):
    account = get_object_or_404(Account, pk=pk)
    serializer = AccountSerializers(account)
    return Response(serializer.data, status=status.HTTP_200_OK)
