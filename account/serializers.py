from rest_framework import serializers

from account.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_number', 'first_name', 'last_name', 'balance', 'account_type']


class AccountCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'pin', 'account_type']
