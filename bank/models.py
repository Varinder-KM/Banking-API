from django.db import models



class Branch(models.Model):
    branch_id = models.IntegerField(blank=False, primary_key=True)
    branch_name = models.CharField(blank=False, max_length=255)
    branch_address = models.CharField(blank=False, max_length=255)
    assets = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return str(self.branch_id)


class Banker(models.Model):
    banker_id = models.IntegerField(blank=False, primary_key=True)
    banker_name = models.CharField(blank=False, max_length=125)
    branch_id = models.ForeignKey(Branch, on_delete= models.CASCADE, related_name='bankers')


class Customer(models.Model):
    customer_id = models.IntegerField(blank=False, primary_key=True)
    customer_name = models.CharField(blank=False, max_length=125)
    dob = models.CharField(blank=False, max_length=12)
    mobileno = models.CharField(blank=False, max_length=10)
    
    def __self__(self):
        return str(self.customer_id)


class Account(models.Model):
    ACC_TYPE = {
        "S": "Savings",
        "C": "Current"
    }
    account_id = models.IntegerField(blank=False, primary_key=True)
    account_balaance = models.DecimalField(max_digits=8, decimal_places=2)
    account_type = models.TextField(max_length=1, choices=ACC_TYPE)
    branch_id = models.ForeignKey(Branch, on_delete= models.CASCADE, related_name='accounts')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return str(self.account_id)





class Transaction(models.Model):
    transaction_id = models.IntegerField(blank=False, primary_key=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    amount  = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return str(self.transaction_id)



class CreditCard(models.Model):
    credit_card_id = models.IntegerField(blank=False, primary_key=True)
    expiry_date = models.CharField(blank=False, max_length=6)
    card_limit  = models.DecimalField(max_digits=8, decimal_places=2)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_cards')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='credit_cards')
    
    def __str__(self):
        return str(self.credit_card_id)



class Loan(models.Model):
    loan_id = models.IntegerField(blank=False, primary_key=True)
    issued_amount =  models.DecimalField(max_digits=8, decimal_places=2)
    remaining_amount =  models.DecimalField(max_digits=8, decimal_places=2)
    branch_id =  models.ForeignKey(Branch, on_delete= models.CASCADE, related_name='loans')
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='loans')

    def __str__(self):
        return str(self.loan_id)

class LoanPayment(models.Model):
    loan_payment_id = models.IntegerField(blank=False, primary_key=True)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='loan_payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.loan_payment_id)

class Borrower(models.Model):
    borrower_id = models.IntegerField(blank=False, primary_key=True)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='loan_borrowers')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loan_borrowds')

    def __str__(self):
        return str(self.borrower_id)