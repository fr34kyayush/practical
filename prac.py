employee = []
c = "y"
while (c=='y'):
    print ("1. PUSH")
    print ("2. POP")
    print ("3. DISPLAY")
    choice = int(input("Enter your choice : "))
    if (choice==1):
        e_id = input("Enter employee no : ")
        name = input("Enter the name : ")
        emp = (e_id,name)
        employee.append(emp)
    elif (choice==2):
        if (employee==[]):
            print("Stack Empty")
        else:
            e_id,name = employee.pop()
            print("Deleted element is : ",e_id,name)
    elif (choice==3):
        i = len(employee)
        while i>0 :
            print(employee[i-1])
            i = i-1
    else:
        print("Wrong Input")
    c = input("Do you want to continue or not(Y/N) : ")
