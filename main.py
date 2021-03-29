dict_student={}
dict_of_marks={}
t={"hindi":' ',"english":' ',"maths":' '}
list_subject=['Hindi','English','Maths']
d={}
df={}
dom={}
#global dictionaries

def menu():
    print('====================================================================')
    print('|        S-T-U-D-E-N-T  M-A-N-A-G-E-M-E-N-T  S-Y-S-T-E-M           |')
    print('====================================================================')
    print('         Enter Choice Number to use the given features:             ')
    print('         1) Add Student'                                             )
    print('         2) Modify Student'                                          )
    print('         3) Display Students List'                                   )
    print('         4) Display Subjects List'                                   )
    print('         5) Update Marks'                                   )
    print('         6) View full Database(Marksheet)'                                           )
    print('         7) View Specific Data'                                      )
    print('         8) Exit'                                                    )
    print('====================================================================')
    choice=int(input('Enter Choice No.'))
    if choice==1:
       if dict_student!={}:
          add_student2()
       else:
          add_student()
    elif choice==2:
         mod_student()
    elif choice==3:
         list_student()
    elif choice==4:
         list_subject()
    elif choice==5:
         update_marks()
    elif choice==6:
         view_database()
    elif choice==7:
         view_specdata()
    elif choice==8:
         exit()
    else:
        print('Invalid Choice!')
         
#all functions
def add_student():     #1
    rollno1=eval(input('Enter Roll No.'))
    name1=input('Enter Name:')
    dict_student[rollno1]=name1
    print('Student added!')
    x=input('Continue?y or n:')
    while x=='n':
          menu()
    while x!='n':
          rollno2=eval(input('Enter Roll No.'))
          temp=dict_student.get(rollno2)
          if temp!= None:
                 print("Student exist in database!")
                 u_i=eval(input('Press 1 for Menu and 2 for add student:=>'))
                 if u_i==1:
                     menu()
                 else:
                    add_student()
                 break
          else:
              name2=input('Enter Name:')
              dict_student[rollno2]=name2
              y=input('Continue?y or n:')
              while y=='n':
                    menu()
def add_student2():
    rn=eval(input('Enter Roll No.'))
    if rn not in dict_student:
       name=input('Enter Name:')
       dict_student[rn]=name
       print('Added Successfully!')
       y=input('Continue?y or n:')
       while y=='n':
             menu()
       while y!='n':
             add_student2()
    else:
       print('Student Exist In Database!')
       y=input('Press 1 for Menu and 2 for Add another student:=>')
       while y=='1':
             menu()
       while y=='2':
             add_student2()


               
                 
def mod_student():   #2
    print('list of students:',dict_student)
    rollno1=eval(input('Enter Roll No.'))
    temp=dict_student.get(rollno1)
    if temp== None:
                 print("Student does not exist in database!")
                 u_i=eval(input('Press 1 for Menu and 2 for modify existing student:=>'))
                 if u_i==1:
                     menu()
                 else:
                    mod_student()
    else:
        name1=input('Enter Name:')
        dict_student[rollno1]=name1
        print('Updated Successfully!')
        x=input('Continue?y or n:')
        while x=='n':
              menu()
        while x!='n':
              rollno2=eval(input('Enter Roll No.'))
              temp=dict_student.get(rollno2)
              if temp== None:
                 print("Student does not exist in database!")
                 u_i=eval(input('Press 1 for Menu and 2 for modify existing student:=>'))
                 if u_i==1:
                     menu()
                 else:
                    mod_student()
                 break
              else:
                  name2=input('Enter Name:')
                  dict_student[rollno2]=name2
                  print('Updated Successfully!')
                  y=input('Continue?y or n:')
                  while y=='n':
                        menu()

def mtidic():
    rn=int(input('Enter Roll No.:'))
    if rn not in dict_student.keys():
       print('Student Not Exist!')
       y=input('Press 1 for Menu and 2 for Update Marks of Existing student:=>')
       while y=='1':
             menu()
       while y=='2':
             Maths()
    else:    
        mk=input('Enter Marks:')
        x=1
        while x<len(dict_student):
              t3={"hindi":dict_of_marks[rn]['hindi'],"english":dict_of_marks[rn]['english'],"maths":' '}
              x=x+2
        t3['maths']=mk
        dict_of_marks[rn]=t3
        print('dict_of_marks',dict_of_marks)


def upddic():
    rn=int(input('Enter Roll No.:'))
    if rn not in dict_student.keys():
       print('Student Not Exist!')
       y=input('Press 1 for Menu and 2 for Update Marks of Existing student:=>')
       while y=='1':
             menu()
       while y=='2':
             English()
    else:
        mk=input('Enter Marks:')
        x=1
        while x<len(dict_student):
              t2={"hindi":dict_of_marks[rn]['hindi'],"english":' ',"maths":' '}
              x=x+2
        t2['english']=mk
        dict_of_marks[rn]=t2
        print('dict_of_marks',dict_of_marks)

def hindi():
    rn=int(input('Enter Roll No.:'))
    if rn not in dict_student.keys():
       print('Student Not Exist!')
       y=input('Press 1 for Menu and 2 for Update Marks of Existing student:=>')
       while y=='1':
             menu()
       while y=='2':
             hindi()
    else:
       mk=input('Enter Marks:')
       t1={"hindi":' ',"english":' ',"maths":' '}
       t1['hindi']=mk
       x=1
       while x<len(dict_student):
             dict_of_marks[rn]=t1
             x=x+1
       print('dict_of_marks',dict_of_marks)
       print('Updated Successfully!')
       y=input('Continue?y or n:')
       while y=='n':
             menu()
       while y!='n':
             hindi()

def English():
    upddic()
    print('Updated Successfully!')
    y=input('Continue?y or n:')
    while y=='n':
          menu()
    while y!='n':
          English()


def Maths():
    mtidic()
    print('Updated Successfully!')
    y=input('Continue?y or n:')
    while y=='n':
          menu()
    while y!='n':
          Maths()

def update_marks():
    print('Enter Choice Number To Select Subject!')
    print('1)Hindi')
    print('2)English')
    print('3)Maths')
    i=int(input('ENTER CHOICE NUMBER==>'))
    if i==1:
        hindi()
    elif i==2:
        English()
    elif i==3:
        Maths()

def list_student():   #3
    print('List of students:',dict_student)
    menu()
    
def list_subject():   #4
    list_subject=['Hindi','English','Maths']
    print('List of subject:',list_subject)
    menu()

def view_database():  #5
    print(dict_of_marks)
    print('FULL MARKSHEET')
    print('==========================================================================================')
    print('|                         F  U  L  L       M  A  R  K  S  H  E  E  T                     |')
    print('==========================================================================================')
    print('|| R O L L N O.   ||    N A M E    ||    H I N D I  ||    E N G L I S H   ||  M A T H S ||')
    j=dict_student.keys()
    k=dict_student.values()
    for i in j:
        for o in k:
            print(i,'                    ',o,'                        ',dict_of_marks[i]['hindi'],"                             ",dict_of_marks[i]['english'],'                                   ',dict_of_marks[i]['maths'])

    

def view_specdata():  #6
    rn=int(input('Enter Roll No.:'))
    if rn not in dict_student.keys():
       print('Student Not Exist!')
       y=input('Press 1 for Menu and 2 for View Marksheet of Existing student:=>')
       while y=='1':
             menu()
       while y=='2':
             view_specdata()
    else:    
        speclist={"hindi":dict_of_marks[rn]['hindi'],"english":dict_of_marks[rn]['english'],"maths":dict_of_marks[rn]['maths']}
        print(speclist)
        print('==========================================================================================')
        print('|             S    T   U   D   E   N   T   M  A  R  K  S  H  E  E  T                     |')
        print('==========================================================================================')
        print('|       ||    H I N D I      ||    E N G L I S H   ||  M A T H S    ||                    |')
        print('|       ||',speclist.get('hindi'),'||                    ||',speclist.get('english'),'||               ||',speclist.get('maths'),'||')
        print('==========================================================================================')
        y=input('Press 1 for Menu and 2 for View Marksheet of Existing student:=>')
        while y=='1':
              menu()
        while y=='2':
              view_specdata()
menu()   







