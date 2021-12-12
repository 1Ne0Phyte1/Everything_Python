import statistics as s
admins = {'Python':'pass123'}
studentDict = {'Jeff':[66,56,45,45,56],
               'Alex':[78,66,56,56,76],
               'Sam':[32,24,34,20]}

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeTOEnter))
    else:
        print('Student does not exits.')
    print(studentDict)
    
            
    def main():
        print("""
        Welcome to  Grade Central

        [1] - Enter Grade
        [2] - Remove Student
        [3] - Student Average Grade
        [4] - Exit
        """)
        action = input('What will you like to do today? (Enter a number)')


        if action =='1':
            enterGrades()
        elif action =='2':
            print('2')
        elif action =='3':
            print('3')
        else:
            print('No valid choice was given,try again')

    login = input('Username: ')
    passw = input('Password: ')

   
        if login in admins:
            if admins[login] == passw:
                print ('Welcome,',login)
                while True:
                    main()
            else:
                    print('Invalid pasword, will detonate in 5 seconds!')

        else:
            print('Invalid username, calling the FBI to report this') 
