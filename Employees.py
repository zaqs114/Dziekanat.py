import Classes
import os

def employee_menu():
    choice = input("""Pracownicy.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby dodać pracownika.
        Wybierz 2 aby usunąć pracownika.
        """)
    if choice == "0":
        employee_write_to_file()
        os.system('cls')
        import Main
        Main.edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_employee()
    if choice == "2":
        os.system('cls')
        delete_employee()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
        """)
        employee_menu()


def employee_write_to_file():
    employees = open("pracownicy.txt", "w")
    for i in Classes.ITEmployee.itEmployeeList:
        employees.write(str(i)+'\n')
    for i in Classes.MathEmployee.mathEmployeeList:
        employees.write(str(i)+'\n')
        employees.close()


def add_employee():
    choice = input("""Dodawanie pracownika.

        Jeśli chcesz dodać informatyka wybierz 1. 
        Jeśli chcesz dodać matematyka wybierz 2. 
        Jeśli nie chcesz dodawać pracownika, wybierz 0.
        """)

    if choice == "0":
        os.system('cls')
        employee_menu()

    if choice == "1":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        salary = input("Podaj wynagrodzenie: ")
        Classes.ITEmployee.itEmployeeList.append(Classes.ITEmployee(name, surname, pesel, salary))
        os.system('cls')
        print("""Pomyślnie dodano pracownika
        """)
        add_employee()
    if choice == "2":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        salary = input("Podaj wynagrodzenie: ")
        Classes.MathEmployee.mathEmployeeList.append(Classes.MathEmployee(name, surname, pesel, salary))
        os.system('cls')
        print("Pomyślnie dodano pracownika")
        print()
        add_employee()

    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        add_employee()


def delete_employee():
    choice = input("""Usuwanie pracownika.
        Jeśli chcesz informatyka, wybierz 1.
        Jesli chcesz matematyka, wybierz 2.
        Jeśli chcesz powrócić do poprzedniego menu, wybierz 0.
        """)

    if choice == "0":
        os.system('cls')
        employee_menu()
    if choice == "1":
        os.system('cls')
        delete_it_employee()
    if choice == "2":
        os.system('cls')
        delete_math_employee()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        delete_employee()


def delete_it_employee():

    try:
        j = 1
        print("Usuwanie informatyka")
        print()
        if not Classes.ITEmployee.itEmployeeList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_employee()

        for i in Classes.ITEmployee.itEmployeeList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.ITEmployee.itEmployeeList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto informatyka.")
        print()
        delete_employee()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_it_employee()


def delete_math_employee():
    try:
        j = 1
        print("Usuwanie matematyka")
        print()
        if not Classes.MathEmployee.mathEmployeeList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_employee()

        for i in Classes.MathEmployee.mathEmployeeList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.MathEmployee.mathEmployeeList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunnięto matematyka.")
        print()
        delete_employee()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_math_employee()