from rest_framework import serializers
from bank.models import (Branch, Banker, Account, Customer, Transaction, CreditCard,
                        Loan, LoanPayment, Borrower)



class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields='__all__'

class LoanSerializer(serializers.ModelSerializer):
    loan_borrowers = BorrowerSerializer(many=True, read_only=True)
    loan_payments = LoanPaymentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Loan
        fields='__all__'



class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'




class AccountSerializer(serializers.ModelSerializer):  
    transactions = TransactionSerializer(many=True, read_only=True)
    credit_cards = CreditCardSerializer(many=True, read_only=True)
    loans = LoanSerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = "__all__"
    
class CustomerSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    credit_cards = CreditCardSerializer(many=True, read_only=True)
    loan_borrowds = BorrowerSerializer(many=True, read_only=True)
    accounts = AccountSerializer(many=True, read_only=True)
    class Meta:
        model=Customer
        fields="__all__"



class BankerSerializer(serializers.Serializer):
    banker_id = serializers.IntegerField()
    banker_name = serializers.CharField()
    
    def create(self, validated_data):
        return Banker.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.banker_id  = validated_data.get('banker_id ', instance.banker_id)
        instance.banker_name = validated_data.get('branch_name', instance.banker_name)
        return instance


class BranchSerializer(serializers.Serializer):
    branch_id = serializers.IntegerField()
    branch_name = serializers.CharField()
    branch_address = serializers.CharField()
    assets = serializers.CharField()

    bankers = BankerSerializer(many=True, read_only=True)
    accounts = AccountSerializer(many=True, read_only=True)
    loans = LoanSerializer(many=True, read_only=True)


    def create(self, validated_data):
        return Branch.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.branch_id = validated_data.get('branch_id', instance.branch_id)
        instance.branch_name = validated_data.get('branch_name', instance.branch_name)
        instance.branch_address = validated_data.get('branch_address', instance.branch_address)
        instance.assets = validated_data.get('assets', instance.assets)
        return instance