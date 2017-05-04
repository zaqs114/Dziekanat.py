import os
import Classes


def start():
    choice=input(""" Witaj w aplikacji dziekanat.
    Wybierz 1 aby edytować informacje.
    Wybierz 2 aby wyświetlić bazę.
    Wybierz 3 aby wyświetlić statystyki.
    Wybierz 0 aby wyjść.
    """)

    if choice == "0":
        exit(0)
    if choice == "1":
        os.system('cls')
        edit_information_menu()
    if choice == "2":
        print("kappa")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        start()


def edit_information_menu():
    choice = input(""" Edycja informacji.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby edytować informacje o studentach.
        """)
    if choice == "0":
        os.system('cls')
        start()
    if choice == "1":
        os.system('cls')
        students_menu()
    if choice == "2":
        print("kappa")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        edit_information_menu()


def students_menu():
    choice=input("""Studenci.
    Wybierz 0 aby powrócić do poprzedniego menu.
    Wybierz 1 aby dodać studenta.
    Wybierz 2 aby usunąć studenta.
    """)
    if choice == "0":
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_student()
    if choice == "2":
        os.system('cls')
        delete_student()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        students_menu()


def add_student():
    choice = input("""Dodawanie studenta.
    
    Jeśli chcesz dodać studenta studiującego w trybie dziennym wybierz 1. 
    Jeśli chcesz dodać studenta studiującego w trybie zaocznym - wybierz 2. 
    Jeśli nie chcesz dodawać studenta, wybierz 0.
    """)

    if choice == "0":
        os.system('cls')
        students_menu()

    if choice == "1":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        studentID = input("Podaj numer indeksu: ")
        Classes.DailyStudent.dailyStudentList.append(Classes.DailyStudent(name, surname, pesel, studentID))
        os.system('cls')
        print("Pomyślnie dodano studenta")
        print()
        add_student()

    if choice == "2":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        studentID = input("Podaj numer indeksu: ")
        Classes.WeekendStudent.weekendStudentList.append(Classes.WeekendStudent(name, surname, pesel, studentID))
        os.system('cls')
        print("Pomyślnie dodano studenta")
        print()
        add_student()

    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        add_student()


def delete_student():

    choice = input("""Usuwanie studenta.
    Jeśli chcesz usunąć studenta dziennego, wybierz 1.
    Jesli chcesz usunąć studenta zaocznego, wybierz 2.
    Jeśli chcesz powrócić do poprzedniego menu, wybierz 0.
    """)

    if choice == "0":
        os.system('cls')
        students_menu()
    if choice == "1":
        os.system('cls')
        delete_daily_student()
    if choice == "2":
        os.system('cls')
        delete_weekend_student()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        delete_student()


def delete_daily_student():
    try:
        j = 1
        print("Usuwanie studenta dziennego")
        print()
        if not Classes.DailyStudent.dailyStudentList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_student()

        for i in Classes.DailyStudent.dailyStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.DailyStudent.dailyStudentList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto studenta.")
        print()
        delete_daily_student()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_daily_student()


def delete_weekend_student():
    try:
        j = 1
        print("Usuwanie studenta zaocznego")
        print()
        if not Classes.WeekendStudent.weekendStudentList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_student()

        for i in Classes.WeekendStudent.weekendStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.WeekendStudent.weekendStudentList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto studenta.")
        print()
        delete_weekend_student()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_weekend_student()




start()
