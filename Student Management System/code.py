Student = list()
Course = list()
while(1):
    print("Welcome to SMS (Student Management System)")
    print("Tell us who you are : ")
    print("1. Student")
    print("2. Admin")
    print("0. Exit")
    print("Enter Your Choice : ", end='')
    x = int(input())
    print('--------------------------------------------------------------------------')
    if(x == 1):
        while(1):
            print("Welcome Student")
            print("1. Register")
            print("2. View Courses")
            print("3. Apply for a Course")
            print("0. Go Back to previous Menu")
            print("Enter Your Choice : ", end='')
            c1 = int(input())
            print(
                '--------------------------------------------------------------------------')
            if(c1 == 1):
                stu = dict()
                print("Enter Roll Number of the Student : ", end='')
                stu['Roll No'] = input()
                print("Enter Name of the Student : ", end='')
                stu['Name'] = input()
                print("Enter Date of Birth of the Student (dd/mm/yyyy) : ", end='')
                stu['DOB'] = input()
                print("Enter Course ID of the Course : ", end='')
                stu['Course ID'] = input()
                print('Student Registered Successfully!!')
                Student.append(stu)
                print(
                    '--------------------------------------------------------------------------')
            elif(c1 == 2):
                for cor in Course:
                    print('S.No. : {0}'.format(Course.index(cor)+1))
                    for i in cor:
                        print(i, ':', cor[i])
                print(
                    '--------------------------------------------------------------------------')
            elif(c1 == 3):
                while(1):
                    c = list()
                    print("0. Go Back to previous Menu")
                    for cor in Course:
                        c.append(cor['Course ID'])
                        print(cor['Name'], ':', cor['Course ID'])
                    print('Enter the Course ID for the Course you want to apply')
                    print('Enter your Choice : ', end='')
                    cid = input()
                    print(
                        '--------------------------------------------------------------------------')
                    if(cid in c or cid == '0'):
                        print('Course Applied Successfully!!')
                        break
                    else:
                        print("Wrong Choice, Please Try Again")
                        print(
                            '--------------------------------------------------------------------------')
            elif(c1 == 0):
                print(
                    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                print(
                    '--------------------------------------------------------------------------')
                break
            else:
                print("Wrong Choice, Please Try Again")
                print(
                    '--------------------------------------------------------------------------')
    elif(x == 2):
        while(1):
            print("Welcome Admin")
            print("1. Add a new Course")
            print("2. View Courses")
            print("3. View Student")
            print("0. Go Back to previous Menu")
            print("Enter Your Choice : ", end='')
            c2 = int(input())
            print(
                '--------------------------------------------------------------------------')
            if(c2 == 1):
                cor = dict()
                print("Enter Course ID of the Course : ", end='')
                cor['Course ID'] = input()
                print("Enter Name of the Course : ", end='')
                cor['Name'] = input()
                print("Enter Duration of the Course : ", end='')
                cor['Duration'] = int(input())
                print("Enter Fees of the Course : ", end='')
                cor['Fees'] = int(input())
                Course.append(cor)
                print('Course Added Successfully!!')
                print(
                    '--------------------------------------------------------------------------')
            elif(c2 == 2):
                for cor in Course:
                    print('S. No. : {0}'.format(Course.index(cor)+1))
                    for i in cor:
                        print(i, ':', cor[i])
                print(
                    '--------------------------------------------------------------------------')
            elif(c2 == 3):
                for stu in Student:
                    print('S. No. : {0}'.format(Student.index(stu)+1))
                    for i in stu:
                        print(i, ':', stu[i])
                print(
                    '--------------------------------------------------------------------------')
            elif(c2 == 0):
                print(
                    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                print(
                    '--------------------------------------------------------------------------')
                break
            else:
                print("Wrong Choice, Please Try Again")
                print(
                    '--------------------------------------------------------------------------')
    elif(x == 0):
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print('--------------------------------------------------------------------------')
        break
    else:
        print("Wrong Choice, Please Try Again")
        print('--------------------------------------------------------------------------')
