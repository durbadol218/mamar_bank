from django.contrib import admin
from .models import TransactionModel
from .views import sendTransactionEmail
# Register your models here.
@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account','amount','balance_after_transaction','transaction_type','loan_approve']
    
    def save_model(self,request,obj,form,change):
        if obj.loan_approve == True:
            obj.account.balance += obj.amount
            obj.balance_after_transaction = obj.account.balance
            obj.account.save()
            sendTransactionEmail(obj.account.user, obj.amount,"Loan Approval",'admin_email.html')
            
        super().save_model(request,obj,form,change)