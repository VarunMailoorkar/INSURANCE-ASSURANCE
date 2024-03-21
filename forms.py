from django import forms
from .models import Customer, Car, Accident, Payment, Policy

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_id', 'name', 'address', 'dob', 'mobile_no', 'email']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['vehicle_id', 'company', 'model', 'colour', 'year', 'plate_no', 'cust_id']

class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = ['accident_id', 'acc_date', 'place', 'field_no', 'damage_tier', 'veh_id']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['pay_id', 'mode', 'amount', 'transaction_date', 'p_no']

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['poly_no', 'date_issued', 'amount', 'cust_id']
