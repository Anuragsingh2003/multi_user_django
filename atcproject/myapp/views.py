from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            is_doctor = form.cleaned_data.get('is_doctor')
            is_patient = form.cleaned_data.get('is_patient')
            user = form.save()

            # Redirect based on the value of is_doctor
            if is_patient:
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('patient_login')
            else:
                user = authenticate(request, username=username, password=password)
                login(request, user)
                request.session['username'] = username  # create session
                return redirect('doctor_login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})



def is_doctor(user):
    return user.is_authenticated and user.is_doctor

@user_passes_test(is_doctor, login_url='/doctor_login/')
def doctor(request):
    return render(request, 'doctor/doctor.html', {'user': request.user})

def is_patient(user):
    return user.is_authenticated and user.is_patient

@user_passes_test(is_patient, login_url='/patient_login/')
def patient(request):
    return render(request, 'patient/patient.html', {'user': request.user})


def patient_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            elif user is not None and user.is_patient: 
                login(request, user)
                request.session['username'] = username  # create session
                return redirect('patient')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'patient_login.html', {'form': form, 'msg': msg})


def patient_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_authenticated and user.is_patient:
                login(request, user)
                request.session['username'] = username  # create session
                return redirect('patient')
            else:
                msg = 'Invalid credentials or not a patient account'
        else:
            msg = 'Error validating form'
    return render(request, 'patient_login.html', {'form': form, 'msg': msg})


def doctor_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_authenticated and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg = {'Invalid credentials or not a doctor account'}
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logt(request):
    logout(request)
    return redirect('index')


from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import User


