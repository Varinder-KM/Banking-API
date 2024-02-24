from django.urls import path
from bank.api.views import (BranchAD, BranchDetail, BankerAD, BankerDetail, AccountAD, 
                        AccountDetail, CustomerAD, CustomerDetail, TransactionAD, TransactionDetail, 
                        CreditCardAD, CreditCardDetail, LoanAD, LoanDetail, LoanPaymentAD, 
                        LoanPaymentDetail, BorrowerAD, BorrowerDetail)
urlpatterns = [
    path('', BranchAD, name='Branch-list'),
    path('branch/', BranchAD, name='Branch-list'),
    path('branch/<int:pk>', BranchDetail, name='Branch-Detail'),
    path('branch/<int:pk>/bankers',  BranchDetail, name='Branch-Detail'),
    path('branch/<int:pk>/accounts',  BranchDetail, name='Branch-Detail'),
    path('branch/<int:pk>/loans',  BranchDetail, name='Branch-Detail'),

    path('bankers/', BankerAD.as_view(), name='Banker-list' ),
    path('bankers/<int:pk>', BankerDetail.as_view(), name='Banker-Detail'),

    path('accounts/', AccountAD.as_view(), name='Account-list' ),
    path('accounts/<int:pk>', AccountDetail.as_view(), name='Account-Detail'),
    path('accounts/<int:pk>/transactions', AccountDetail.as_view(), name='Account-Detail'),
    path('accounts/<int:pk>/creditcards', AccountDetail.as_view(), name='Account-Detail'),
    path('accounts/<int:pk>/loans', AccountDetail.as_view(), name='Account-Detail'),

    path('customers/', CustomerAD.as_view(), name='Customer-list'),
    path('customers/<int:pk>', CustomerDetail.as_view(), name='Customer-Detail'),
    path('customers/<int:pk>/accounts', CustomerDetail.as_view(), name='Customer-Detail'),
    path('customers/<int:pk>/transactions', CustomerDetail.as_view(), name='Customer-Detail'),
    path('customers/<int:pk>/creditcard', CustomerDetail.as_view(), name='Customer-Detail'),
    path('customers/<int:pk>/loan-borrowds', CustomerDetail.as_view(), name='Customer-Detail'),

    path('transactions/', TransactionAD.as_view(), name='Transaction-list'),
    path('transactions/<int:pk>', TransactionDetail.as_view(), name='Transaction-Detail'),

    path('CreditCards/', CreditCardAD.as_view(), name='Credit-Card-list'),
    path('CreditCards/<int:pk>', CreditCardDetail.as_view(), name='Credit-Card-list'),

    path('CreditCards/', CreditCardAD.as_view(), name='Credit-Card-list'),
    path('CreditCards/<int:pk>', CreditCardDetail.as_view(), name='Credit-Card-Detail'),

    path('Loan/', LoanAD.as_view(), name='Loan-list'),
    path('Loan/<int:pk>', LoanDetail.as_view(), name='Loan-Detail'),
    path('Loan/<int:pk>/borrowed', LoanDetail.as_view(), name='Loan-Detail'),
    path('Loan/<int:pk>/payed', LoanDetail.as_view(), name='Loan-Detail'),

    path('Loan-payment/', LoanPaymentAD.as_view(), name='LoanPayment-list'),
    path('Loan-payment/<int:pk>', LoanPaymentDetail.as_view(), name='LoanPayment-Detail'),

    path('Borrower/', BorrowerAD.as_view(), name='Borrower-list'),
    path('Borrower/<int:pk>', BorrowerDetail.as_view(), name='Borrower-Detail'),
]