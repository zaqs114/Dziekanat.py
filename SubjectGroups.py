import Classes
import os


def subject_groups_menu():
    choice = input("""Grupy przediotowe.
                Wybierz 0 aby powrócić do poprzedniego menu.
                Wybierz 1 aby dodać grupe przedmiotową.
                Wybierz 2 aby usunąć grupę przedmiotową.
                """)
    if choice == "0":
        os.system('cls')
        import Main
        Main.edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_subject_group()

    if choice == "2":
        os.system('cls')
        delete_subject_group()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
            """)
        subject_groups_menu()


def check_tables():
    if not Classes.Subjects.subjectList:
        j=1;
    else:
        j=0;
    if not Classes.WeekendStudent.weekendStudentList:
        j=1;
    else:
        j=0;
    if not Classes.DailyStudent.dailyStudentList:
        j=1;
    else:
        j=0;
    if not Classes.ITEmployee.itEmployeeList:
        j=1;
    else:
        j=0;
    if not Classes.MathEmployee.mathEmployeeList:
        j=1;
    else:
        j=0;
    return j


def add_subject_group():
    j=check_tables()
    if j==1:
        choice = input("""W bazie nie ma wystarczającej ilości danych. Wybierz cokolwiek aby powrócić.
                    """)
        os.system('cls')
        subject_groups_menu()
    print("Dodawanie grupy przedmiotowej.")
    subjectGroupID=input("""Wprowadź oznaczenie grupy
    """)
    if not Classes.Subjects.subjectList:
        choice = input("""W bazie nie ma żadnego przedmiotu. Dodaj jakiś i spróbuj ponownie. Wybierz cokolwiek aby powrócić.
                    """)
        os.system('cls')
        subject_groups_menu()

    j = 1
    for i in Classes.Subjects.subjectList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz przedmiot dla którego chcesz utworzyć nową grupę..
                """))
    choice -= 1
    subjectGroupName = Classes.Subjects.subjectList[choice].subjectName
    subjectgroups = open("grupyprzedmiotowe.txt", "a")
    subjectgroups.write(subjectGroupID+"\t")
    subjectgroups.write(subjectGroupName+"\t")
    subjectgroups.close()

    os.system('cls')
    choice=int(input("""Dodawanie grupy przedmiotowej.
    Wybierz 1 aby dodać informatyka do grupy.
    Wybierz 2 aby dodać matematyka do grupy
    """))
    if choice==1:
        os.system('cls')
        add_itemployee_to_group()
        choice = int(input("""Dodawanie grupy przedmiotowej.
                            Wybierz 1 aby studentów dziennych do grupy.
                            Wybierz 2 aby studentów zaocznych do grupy
                            """))
        if choice == 1:
            add_daily_student_to_group()


        if choice==2:
            add_weekend_student_to_group()

    if choice == 2:
        os.system('cls')
        add_mathemployee_to_group()
        choice = int(input("""Dodawanie grupy przedmiotowej.
                            Wybierz 1 aby dodać studentów dziennych do grupy.
                            Wybierz 2 aby dodać studentów zaocznych do grupy
                            """))
        if choice == 1:
            add_daily_student_to_group()

        if choice == 2:
            add_weekend_student_to_group()

    subjectgroups = open("grupyprzedmiotowe.txt", "a")
    subjectgroups.write("\n")
    subjectgroups.close()
    os.system('cls')
    print("Pomyślnie dodano grupe przedmiotowa")
    print()
    subject_groups_menu()


def add_itemployee_to_group():
    if not Classes.ITEmployee.itEmployeeList:
        os.system('cls')
        print("W bazie nie ma żadnych pracowników. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.ITEmployee.itEmployeeList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                        """))
    choice -= 1
    teacherName = Classes.ITEmployee.itEmployeeList[choice].firstname + " " + Classes.ITEmployee.itEmployeeList[choice].lastname
    subjectgroups = open("grupyprzedmiotowe.txt", "a")
    subjectgroups.write(teacherName+"\t")
    subjectgroups.close()


def add_mathemployee_to_group():
    if not Classes.MathEmployee.mathEmployeeList:
        os.system('cls')
        print("W bazie nie ma żadnych pracowników. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.MathEmployee.mathEmployeeListt:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                        """))
    choice -= 1
    teacherName = Classes.MathEmployee.mathEmployeeList[choice].firstname + " " + Classes.MathEmployee.mathEmployeeList[choice].lastname
    subjectgroups = open("grupyprzedmiotowe.txt", "a")
    subjectgroups.write(teacherName + "\t")
    subjectgroups.close()


def add_daily_student_to_group():
    if not Classes.DailyStudent.dailyStudentList:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.DailyStudent.dailyStudentList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz studenta którego chcesz dodać do grupy
                """))
    choice -= 1
    nameOfStudent = Classes.DailyStudent.dailyStudentList[choice].firstname + " " + Classes.DailyStudent.dailyStudentList[choice].lastname
    subjectgroups = open("grupyprzedmiotowe.txt", "a")
    subjectgroups.write(nameOfStudent + "\t")
    subjectgroups.close()

    choice=input("""
    Wybierz 1 aby dodać kolejnego studenta.
    Wybierz cokolwiek aby powrócić""")
    if choice == "1":
        add_daily_student_to_group()



def add_weekend_student_to_group():
    if not Classes.WeekendStudent.weekendStudentList:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.WeekendStudent.weekendStudentList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz studenta którego chcesz dodać do grupy
                   """))
    choice -= 1
    nameOfStudent = Classes.WeekendStudent.weekendStudentList[choice].firstname + " " + Classes.WeekendStudent.weekendStudentList[choice].lastname
    subjectgroups = open("grupyprzedmiotowe.txt", "a1")
    subjectgroups.write(nameOfStudent + "\t")
    subjectgroups.close()
    choice = input("""
       Wybierz 1 aby dodać kolejnego studenta.
       Wybierz 0 aby powrócić""")
    if choice == "1":
        add_daily_student_to_group()


def delete_subject_group():
    print("Usuwanie grupy przedmiotowej: ")
    list = []
    with open("grupyprzedmiotowe.txt", "r") as textobj:
        j=1
        for i in textobj:
            print(str(j) + ". " + i)
            j=j+1
            list.append(i)
    if not list:
        choice = int(input("Wybierz którą pozycję chcesz usunąć."))
        list.pop(choice-1)  # delete regarding element

    # rewrite the textfile from list contents/elements:
    with open("grupyprzedmiotowe.txt", "w") as textobj:
        for n in list:
            textobj.write(n)
    os.system('cls')
    print("Pomyślnie usunięto grupe przedmiotową")
    print()
    subject_groups_menu()
