from django import forms
from .models import TransactionModel

class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount', 'transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') #account taake er kore anbo!
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True #1st a ai field ta disabled thaakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() #User er theke hide kora thaakbe!
        
    def save(self, commit=True):
        self.instance.account = self.account # jei user ta request kortese tar kono object db te thakle tar instance er account a jabo giye ai kaajta ta korbo!
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    
class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter/update korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fillup kora form theke amra amount field er value ke niye ashlam! (Example: 500)
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return amount
    
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account # user er BankAccount
        min_withdraw_amount = 500
        max_withdraw_amount = 100000
        balance = account.balance
        amount = self.cleaned_data.get('amount')  # user er fillup kora form theke amra amount field er value ke niye ashlam! (Example: 500)
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )
        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f"You've {balance} $ in your account. "
                "You can't withdraw more than your account balance"
            )
        return amount
    
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        
        return amount