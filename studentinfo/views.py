from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def student_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        student = Student(name=name, age=age, email=email, address=address)
        student.save()
        
        return redirect('student_view') 
    
    return render(request, 'studentinfo/student_info.html')
