import os
import Students
import Employees
import Subjects
import SubjectGroups


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
        os.system('cls')
        show_base_menu()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        start()


def edit_information_menu():
    choice = input(""" Edycja informacji.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby edytować informacje o studentach.
        Wybierz 2 aby edytować informacje o pracownikach.
        Wybierz 3 aby edytować informacje o przedmiotach.
        Wybierz 4 aby edytować informacje o grupach przedmiotów.
        """)
    if choice == "0":
        os.system('cls')
        start()
    if choice == "1":
        os.system('cls')
        Students.students_menu()
    if choice == "2":
        os.system('cls')
        Employees.employee_menu()
    if choice == "3":
        os.system('cls')
        Subjects.subjects_menu()
    if choice == "4":
        os.system('cls')
        SubjectGroups.subject_groups_menu()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        edit_information_menu()


def show_base_menu():
    choice = input(""" Wyświetlanie bazy.
            Wybierz 0 aby powrócić do poprzedniego menu.
            Wybierz 1 aby wyświetlić informacje o studentach.
            Wybierz 2 aby wyświetlić informacje o pracownikach.
            Wybierz 3 aby wyświetlić informacje o przedmiotach.
            Wybierz 4 aby wyświetlić informacje o grupach przedmiotów.
            """)
    if choice == "0":
        os.system('cls')
        start()
    if choice == "1":
        os.system('cls')
        Students.show_students()
    if choice == "2":
        os.system('cls')
        Employees.show_employees()
    if choice == "3":
        os.system('cls')
        Subjects.show_subjects()
    if choice == "4":
        os.system('cls')
        SubjectGroups.show_subject_groups()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        edit_information_menu()


start()
