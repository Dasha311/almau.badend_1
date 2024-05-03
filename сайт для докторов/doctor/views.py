from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor, Appointment
from .forms import DoctorForm, AppointmentForm
from django.core.paginator import Paginator

def doctor_list(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctor/doctor-list.html', {'doctor': doctor})

def doctor_details(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor-details.html', {'doctor': doctor})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor created successfully.')
            return redirect('doctor-list')
    else:
        form = DoctorForm()
    return render(request, 'doctor/create-doctor.html', {'form': form})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully.')
            return redirect('doctor-details', pk=pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor/edit-doctor.html', {'form': form, 'doctor': doctor})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully.')
        return redirect('doctor_list')
    return render(request, 'doctor/delete-doctor.html', {'doctor': doctor})

def appointments_list(request):
    appointments = Appointment.objects.all()
    paginator = Paginator(appointments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'doctor/appointment-list.html', {'appointments': page_obj})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointments-list')
    else:
        form = AppointmentForm()
    return render(request, 'doctor/create-appointment.html', {'form': form})

def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('appointments_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'doctor/edit-appointment.html', {'form': form, 'appointment': appointment})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('appointments_list')
    return render(request, 'doctor/delete-appointment.html', {'appointment': appointment})


def index_page_view(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_page')
    return render(request, 'doctor/index.html', {'form': form})