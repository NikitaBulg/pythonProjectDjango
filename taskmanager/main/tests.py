from django.test import TestCase

# Create your tests here.
from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)

class LoanAccount(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_debt = models.DecimalField(max_digits=10, decimal_places=2)

class FinancialTransaction(models.Model):
    loan_account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2)
