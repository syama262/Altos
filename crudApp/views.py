from django.shortcuts import redirect,render

from crudApp.models import Employee_Details

# Create your views here.
# To display the registration page .That means to load 'addEmployee.html'
def show_regform(request):
    return render(request,'addEmployee.html')

#to add the employee details to employee_details table
def add_employeeDetails(request):
    if request.method=='POST':
        ename=request.POST['empname']  #the employee name given by the user in the text field with name ='empname'
        emailid=request.POST['email_id']
        phone=request.POST['phno']
        des=request.POST['desig']
        sal=request.POST['salary']

    employee=Employee_Details(emp_name=ename,
                              emp_email=emailid,
                              emp_phone=phone,
                              emp_designation=des,
                              emp_salary=sal)

    employee.save()
    print("saved")
    # to display the same page use redirect() as given below
    #return redirect('/') 
    return redirect('show_employeeDetails') 

#to display or load  the employee details
def show_employeeDetails(request):
    employees=Employee_Details.objects.all()
    return render(request,'showEmployee.html',{'emps':employees})   # emps is the key of the dictionary ( returning value using context)

# to load the details of employees to be edited
def editPage(request,pk):
    employee=Employee_Details.objects.get(id=pk)
    return render(request,'editEmployee.html',{'emps':employee})

#method to edit Employee Details
def edit_employeeDetails(request,pk):
    if request.method=='POST':
        employee=Employee_Details.objects.get(id=pk)
        employee.emp_name=request.POST.get('empname')
        employee.emp_email=request.POST.get('email_id')
        employee.emp_phone=request.POST.get('phno')
        employee.emp_designation=request.POST.get('desig')
        employee.emp_salary=request.POST.get('salary')
        employee.save()
        return redirect('show_employeeDetails')
    return render(request,'editEmployee.html')

# to load the details of employees to be deleted
def deletePage(request,pk):
    employee=Employee_Details.objects.get(id=pk)
    return render(request,'deleteEmployee.html',{'emps':employee})

def delete_Employee(request,pk):
    employee=Employee_Details.objects.get(id=pk)
    employee.delete()
    return redirect('show_employeeDetails') 

                        