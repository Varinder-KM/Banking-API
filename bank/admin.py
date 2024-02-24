from django.contrib import admin
from bank.models import *

admin.site.register(Branch)
admin.site.register(Banker)
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(CreditCard)
admin.site.register(Loan)
admin.site.register(LoanPayment)
admin.site.register(Borrower)