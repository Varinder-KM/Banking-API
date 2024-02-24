from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import mixins
from rest_framework import generics
from bank.api.permissions import AdminOrReadOnly
from bank.models import (Branch, Banker, Account, Customer, Transaction, CreditCard,
                        Loan, LoanPayment, Borrower)

from bank.api.serializers import (BranchSerializer, BankerSerializer, AccountSerializer, 
                            CustomerSerializer, TransactionSerializer, CreditCardSerializer,
                            LoanSerializer, LoanPaymentSerializer, BorrowerSerializer)



# BorrowerSerializer Views
class BorrowerAD(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BorrowerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





# LoanPayment Views
class LoanPaymentAD(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LoanPaymentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






# Loan Views
class LoanAD(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LoanDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







# Credit Card Views
class CreditCardAD(APIView):
    def get(self, request):
        cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreditCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class CreditCardDetail(APIView):
    def get(self, request,pk):
        cards = CreditCard.objects.get(pk=pk)
        serializer = CreditCardSerializer(cards)
        return Response(serializer.data)

    def put(self, request, pk):
        cards = CreditCard.objects.get(pk=pk)
        serializer = CreditCardSerializer(cards, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        cards = CreditCard.objects.get(pk=pk)
        cards.delete()
        return Response(status= status.HTTP_202_ACCEPTED)








# Transaction Views
class TransactionAD(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class TransactionDetail(APIView):
    def get(self, request,pk):
        transactions = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transactions)
        return Response(serializer.data)

    def put(self, request, pk):
        transactions = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transactions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        transactions = Transaction.objects.get(pk=pk)
        transactions.delete()
        return Response(status= status.HTTP_202_ACCEPTED)






# Customer Views
class CustomerAD(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class CustomerDetail(APIView):
    def get(self, request,pk):
        customers = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)

    def put(self, request, pk):
        customers = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        customers = Customer.objects.get(pk=pk)
        customers.delete()
        return Response(status= status.HTTP_202_ACCEPTED)












# Account Views
class AccountAD(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class AccountDetail(APIView):
    def get(self, request,pk):
        accounts = Account.objects.get(pk=pk)
        serializer = AccountSerializer(accounts)
        return Response(serializer.data)

    def put(self, request, pk):
        accounts = Account.objects.get(pk=pk)
        serializer = AccountSerializer(accounts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        accounts = Account.objects.get(pk=pk)
        accounts.delete()
        return Response(status= status.HTTP_202_ACCEPTED)









# Bankers Views
class BankerAD(APIView):
    def get(self, request):
        bankers = Banker.objects.all()
        serializer = BankerSerializer(bankers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class BankerDetail(APIView):
    def get(self, request,pk):
        bankers = Banker.objects.get(pk=pk)
        serializer = BankerSerializer(bankers)
        return Response(serializer.data)

    def put(self, request, pk):
        bankers = Banker.objects.get(pk=pk)
        serializer = BankerSerializer(bankers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        bankers = Banker.objects.get(pk=pk)
        bankers.delete()
        return Response(status= status.HTTP_202_ACCEPTED)





# Branch Views
@api_view(['GET', 'POST'])
@permission_classes([AdminOrReadOnly])
def BranchAD(request):
    if request.method == 'GET':
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AdminOrReadOnly])
def BranchDetail(request, pk):
    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found'}, status= status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    if request.method == 'Put':
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method=='DELETE':
        branch.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
