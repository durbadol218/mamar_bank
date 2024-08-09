from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE
# Create your models here.

# Akta User Deposit, Withdraw, Loan agula korte paarbe!

class TransactionModel(models.Model):
    # akjon user er multiple type transactions hoite paare!
    account = models.ForeignKey(UserBankAccount, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=15)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null= True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False, null= True)
    
    class Meta:
        ordering = ['timestamp']