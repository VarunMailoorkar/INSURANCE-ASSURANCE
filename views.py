# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.core.exceptions import ValidationError

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']  # Corrected typo in variable name
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard upon successful login
            return redirect('dashboard')  # Corrected URL name
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})  # Corrected error message
    else:
        return render(request, 'login.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        # Optionally, you can handle other fields of the User model here
        if user is not None:
            login(request, user)
            # Add success message
            messages.success(request, 'Registration successful. Welcome to Car Insurance!')
            # Redirect to the dashboard after registration
            return redirect('dashboard')  # Corrected URL name
        else:
            # Return an error message if registration fails.
            return render(request, 'register.html', {'error': 'Registration failed'})
    else:
        return render(request, 'register.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'policy_list.html', {'policies': policies})

from django.core.exceptions import ValidationError

def policy_create(request):
    if request.method == 'POST':
        poly_no = request.POST.get('poly_no')
        date_issued = request.POST.get('date_issued')
        price = request.POST.get('Price')  # Corrected variable name
        cust_id = request.POST.get('Cust_id')
        
        try:
            price = float(price)  # Convert input to float
        except ValueError:
            raise ValidationError('“Price” value must be a decimal number.')

        customer = Customer.objects.get(pk=cust_id)

        Policy.objects.create(
            poly_no=poly_no,
            date_issued=date_issued,
            amount=price,  # Corrected variable name
            cust_id=customer
        )

        return redirect('policy_list')
    else:
        form = PolicyForm()
    return render(request,'policy_new.html',{'form':form})

def vehicle_lookup(request):
    # Fetch all vehicles from the database
    vehicles = Car.objects.all()
    return render(request, "vehicle_list.html", {'vehicles': vehicles})

    

def vehicle_add(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        company = request.POST.get('company')
        model = request.POST.get('model')  # Corrected
        colour = request.POST.get('colour')  # Corrected
        year = request.POST.get('makeyear')  # Corrected
        plate_no = request.POST.get('Plate_no')  # Corrected
        cust_id = request.POST.get('Cust_id')
        customer = Customer.objects.get(pk=cust_id)

        Car.objects.create(
            vehicle_id=vehicle_id,
            company=company,
            model=model,
            colour=colour,
            year=year,
            plate_no=plate_no,
            cust_id=customer  # Corrected
        )

        return redirect('vehicle_list')
    else:
        form = CarForm()
    return render(request, 'vehicle_reg.html', {'form': form})


def customer_add(request):
    if request.method == 'POST':
        customer_id = request.POST.get('Customer_id')
        name = request.POST.get('name')
        address = "address"
        dateofbirth = request.POST.get('dateofbirth')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        Customer.objects.create(
            cust_id = customer_id,
            name =name,
            address = address,
            dob = dateofbirth,
            mobile_no = mobile,
            email = email
        )

        return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})


def customer_list(request):
    # Fetch all customers from the database
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def accident_new(request):
    if request.method=='POST':
        accident_id = request.POST.get('accident_id')
        acc_date = request.POST.get('acc_date')
        place = request.POST.get('place')
        field_no = request.POST.get('field_no')
        damage_tier = request.POST.get('damage_tier')
        veh_id = request.POST.get('vehicle_id')
        vehicle = Car.objects.get(pk=veh_id)

        Accident.objects.create(
            accident_id = accident_id,
            acc_date =acc_date,
            place = place,
            field_no = field_no,
            damage_tier = damage_tier,
            veh_id = vehicle
        )

        return redirect('accident_list')
    else:
        form=AccidentForm()
    return render(request,'accident_new.html',{'form':form})

def accident_list(request):
    # Fetch all accidents from the database
    accidents = Accident.objects.all()
    return render(request, 'accident_list.html', {'accidents': accidents})


def pay_list(request):
    # Fetch all payments from the database
    payments = Payment.objects.all()
    return render(request, 'pay_list.html', {'payments': payments})


def pay_record(request):
    if request.method == 'POST':
        pay_id = request.POST.get('payment_id')
        mode = request.POST.get('mode_of_payment')
        transaction_date = request.POST.get('transaction_date')
        pno = request.POST.get('policy_bought')
        policy = Policy.objects.get(pk=pno)

        # Attempt to convert the amount to a float
        try:
            amount = float(request.POST.get('amount'))
        except (TypeError, ValueError):
            amount = 0.0  # Setting a default value

        # Create the Payment object
        Payment.objects.create(
            pay_id=pay_id,
            mode=mode,
            amount=amount,
            transaction_date=transaction_date,
            p_no=policy
        )

        return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'pay_record.html', {'form': form})




