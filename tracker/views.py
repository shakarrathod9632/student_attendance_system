from django.shortcuts import render
from .models import Student, Attendance
from datetime import date

def home(request):
    return render(request, 'home.html')

def students(request):
    data = Student.objects.all()
    return render(request, 'students.html', {'students': data})

def attendance(request):
    data = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance.html', {'attendance': data})

def stats(request):
    total = Student.objects.count()
    present = Attendance.objects.filter(status='Present').count()
    absent = Attendance.objects.filter(status='Absent').count()
    late = Attendance.objects.filter(status='Late').count()

    return render(request, 'stats.html', {
        'total': total,
        'present': present,
        'absent': absent,
        'late': late
    })


