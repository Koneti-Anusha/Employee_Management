from validations import *
class project:
    EmpDict={}
    def __init__(self,emp_id,emp_name,salary,age,gender,address,city,dob,doj,dept_name,desig,pan,aadhar):
        self.Emp_id=emp_id
        self.Emp_name=emp_name
        self.Salary=salary
        self.age=age
        self.gender=gender
        self.address=address
        self.city=city
        self.dob=dob
        self.doj=doj
        self.Dname=dept_name
        self.Designation=desig
        self.pan=pan
        self.aadhar=aadhar
        if self.Dname in self.EmpDict.keys():
            self.EmpDict[self.Dname].append(self.Emp_name)
        else:
            self.EmpDict[self.Dname]=[self.Emp_name]

    def display(self):
        print(self.Emp_id,"",self.Emp_name,"",self.Salary,"",self.age,"",self.gender,"",self.address,"",self.city,"",self.dob,"",self.doj,"",self.Dname,"",self.Designation,"",self.pan,"",self.aadhar)

    @classmethod
    def DisplayDepartment(self):
        for k,v in self.EmpDict.items():
            print("department details",k)
            for ename in v:
                print(ename,end="")
            print("")

Emplist=[]
print("Employee ManageMent System")
print("")
while True:
    print("")
    print("1.Add an Employee")
    print("2.Delete a record")
    print("3.Update an employee details")
    print("4.Search the record")
    print("5.Display details of an Employee with highest salary")
    print("6.Display details of an Employee with lowest salary")
    print("7.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        while True:
            emp_id = input("Enter Employee ID: ")
            if any(employee.Emp_id == emp_id for employee in Emplist):
                print("Invalid: Employee ID already exists. Please enter a new ID.")
            elif isIdValid(emp_id):
                break
            else:
                print("Invalid: Please enter a correct ID.")

        while True:
            emp_name=input("Enter Employee Name: ")
            if isNameValid(emp_name):
                break
            else:
                print("Invalid Name!!! please enter correct name")
        while True:
            salary=input("Enter Salary: ")
            if isSalValid(salary):
                break
            else:
                print("Invalid Salary!!!please enter correct Salary")
        while True:
            age=input("Enter Age: ")
            if isAgeValid(age):
                break
            else:
                print("Invalid age!!!please enter correct age")
        while True:
            gender=input("Enter Gender: ")
            if isGenderValid(gender):
                break
            else:
                print("Invalid age!!!please enter correct gender as Male,Female,Other,binary")
        while True:
            address=input("Enter Address: ")
            if isAddressValid(address):
                break
            else:
                print("Invalid Address!!!please enter correct address")
        while True:
            city=input("Enter City: ")
            if isCityValid(city):
                break
            else:
                print("Invalid city!!!please enter correct city")
        while True:
            dob=input("Enter DOB: ")
            if isDobValid(dob):
                break
            else:
                print("Invalid D.O.B!!!Please enter correct D.O.B")
        while True:
            doj=input("Enter DOJ: ")
            if isDobValid(doj):
                break
            else:
                print("Invalid D.O.J!!!Please enter correct D.O.J")
        while True:
            dept_name=input("Enter Department Name: ")
            if isDnameValid(dept_name):
                break
            else:
                print("Invalid Department Name!!!Please enter correct name")
        while True:
            desig=input("Enter designation: ")
            if isDesiValid(desig):
                break
            else:
                print("Invalid Designation!!!Please enter correct designation")
        while True:
            pan=input("Enter PAN Card Number: ")
            if isPanValid(pan):
                break
            else:
                print("Invalid PAN Number!!!Please enter correct PAN number")
        while True:
            aadhar=input("Enter Aadhar Card number: ")
            if isAadharValid(aadhar):
                break
            else:
                print("Invalid Aadhar Number!!!Please enter correct Aadhar Card Number")
        Employee=project(emp_id,emp_name,salary,age,gender,address,city,dob,doj,dept_name,desig,pan,aadhar)
        Emplist.append(Employee)

    elif choice==2:
        print("")
        print("Press A to delete by Employee Id")
        print("Press B to delete by Employee Name")
        ch=input("Enter your choice")
        if ch=="A":
            while True:
                if len(Emplist)<0:
                    print("List is Empty")
                else:
                    id1=input("Enter the Emp_id to be deleted")
                    if isIdValid(id1):
                        found=False
                        for i in Emplist:
                            if i.Emp_id==id1:
                                Emplist.remove(i)
                                found=True
                                break   
                        if found:
                            for k,v in project.EmpDict.items():
                                if i.Emp_name in v:
                                    v.remove(i.Emp_name)
                            print("Record deleted succesfully")
                        else:
                            print("Record doesn't exist")
                    break
        elif ch=="B":
            while True:
                if len(Emplist)<0:
                    print("List is Empty")
                else:      
                    name=input("enter the name to be deleted")
                    if isNameValid(id1):
                        found=false
                        for i in Emplist:
                            if i.Emp_name==name:
                                Emplist.remove()
                                found=True
                                break
                        if found:
                            for k,v in project.EmpDict.items():
                                if i.Emp_name in v:
                                    v.remove(i.Emp_name)
                            print("Record deleted succesfully")
                        else:
                            print("Record doesn't exist")
                    break

        else:
            print("Invalid choice !! Please enter valid choice")


    elif choice==3:
                    print("")
                    print("A.Update the name")
                    print("B.Update Address")
                    print("C.Update D.O.B")
                    print("D.Update Salary")
                    print("E.Exit")
                    ch=input("Enter your choice")
                    if ch=="A":
                        while True:
                            id=input("Enter the Employee id to update: ")
                            for i in Emplist:
                                if i.Emp_id==id:
                                    name=input("Enter the name you want to update: ")
                                    if isNameValid(name):
                                        i.Emp_name=name
                                        print("name updated Succesfully")
                                    else:
                                        print("Invalid name!! Enter name again")
                                else:
                                    print("employee does not exist:")
    
                    elif ch=="B":
                        while True:
                            id=input("Enter the Employee id to update: ")
                            for i in Emplist:
                                if i.Emp_id==id:
                                    Address=input("Enter the new address: ")
                                    if AddressValid(Address):
                                        i.address=Address
                                        print("Address updated succesfully")
                                    else:
                                        print("Invalid Address!!! Please enter again")
                                else:
                                    print("Employee does not exist:")

                    elif ch=="C":
                        while True:
                            id=input("Enter the Employee id to update: ")
                            for i in Emplist:
                                if i.Emp_id==id:
                                    dob=input("Enter the new Date of Birth: ")
                                    if isDobValid(dob):
                                        i.dob=dob
                                        print("Date of Birth updated succesfully")
                                    else:
                                        print("Invalid dob!!! enter again")
                                else:
                                    print("employee  does not exist:")

                    elif ch=="D":
                        while True:
                            print("select in which you want to update")
                            print("D1.Update salary of specific")
                            print("D2.Update salary of all employees working in specific department")
                            print("D3.Update the salary of all employees")
                            print("D4.Exit")
                            ch1=input("Enter your choice: ")
                            if ch1=="D1":
                                while True:
                                    id1=input("Enter the Employee id to update: ")
                                    if isIdValid(id1):
                                        for i in Emplist:
                                            if i.Emp_id==id1:
                                                sal=input("Enter new salary: ")
                                                if isSalValid(sal):
                                                    i.Salary=sal
                                                    print("Salary updated succesfully")
                                                else:
                                                    print("Invalid Salary!!! Enter again")
                                            else:
                                                print("employee not exist:")
                                    else:
                                        print("Invalid Id enter correct Id")
                            elif ch1=="D2":
                                while True:
                                    dname=input("Enter the Department name in which you want to update salary: ")
                                    sal=input("Enter the new Salary: ")
                                    if isSalValid(sal):
                                        flag=False
                                        for i in Emplist:
                                            if i.Dname==dname:
                                                i.Salary=sal
                                                flag=True
                                        if flag:
                                            print("salary updated succesfully")
                                        else:
                                            print("No employee found in department")
                                    else:
                                        print("Invalid Salary!!!Enter again")
                            elif ch1=="D3":
                                while True:
                                    sal=input("Enter new salary: ")
                                    if isSalValid(sal):
                                        for i in Emplist:
                                            i.Salary=sal
                                            print("Salary updated succesfully")
                                    else:
                                        print("Invalid Salary!!!Enter again")
                            elif ch1=="D4":
                                break
                            else:
                                print("invalid choice!!! Please enter correct choice")
                            
                    elif ch=="E":
                        break

                    else:
                        print("Invalid Choice!!! Please enter valid choice")
                                    
                            

        
    
    elif choice==4:
        print("")
        print("Press A to search by Emp_Id")
        print("Press B to search by Emp_Name")
        print("Press C to search by Department name")
        ch=input("Enter your choice: ")
        if(ch=="A"): 
            id1=input("Enter the Emp_id to be searched: ")
            if isIdValid(id1):
                for i in Emplist:
                    if i.Emp_id==id1:
                        i.display()
                            
        elif(ch=="B"):
            name=input("Enter the Emp_name to be searched: ")
            if isNameValid(name):
                for i in Emplist:
                    if i.Emp_name==name:
                        i.display()
        elif(ch=="C"):
            Dname=input("Enter the department name to search the employee:")
            if isDnameValid(Dname):
                for i in Emplist:
                    if i.Dname==Dname:
                        i.display()
        else:
            print("Invalid Choice!!! Please enter a valid choice:")
                
    
    elif choice==5:
        max=0
        for i in Emplist:
            if int(i.Salary)>0:
                max=i.Salary
        for i in Emplist:
            if int(i.Salary==max):
                print("Employee with highest Salary is: ")
                i.display()
        
    elif choice==6:
        min=9999999
        for i in Emplist:
            if int(i.Salary)<min:
                min=int(i.Salary)
        print("Employee with lowest Salary is: ")
        for i in Emplist:
            if int(i.Salary)==min:
                i.display()

            
    elif choice==7:
        break
        
    else:
        print("Invalid choice!!! Please enter valid choice")
        
            
    
