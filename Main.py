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
        edit_information_menu()
    if choice == "2":
        print("kappa")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        start()


def edit_information_menu():
    os.system('cls')
    choice = input(""" Edycja informacji.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby edytować informacje o studentach.
        """)
    if choice == "0":
        start()
    if choice == "1":
        students_menu()
    if choice == "2":
        print("kappa")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        edit_information_menu()


def students_menu():
    os.system('cls')
    choice=input("""Studenci.
    Wybierz 0 aby powrócić do poprzedniego menu.
    Wybierz 1 aby dodać studenta.
    Wybierz 2 aby usunąć studenta.
    """)
    if choice == "0":
        edit_information_menu()
    if choice == "1":
        add_student()
    if choice == "2":
        print("usuwanie studenta")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        students_menu()


def add_student():
    os.system('cls')
    print("Dodawanie studenta.")
    choice=input("Dzienny czy Zaoczny?")
    if choice == "Dzienny":
        name=input("Podaj imię:")
        surname=input("Podaj nazwisko: ")
        pesel=input("Podaj pesel: ")
        studentID=input("Podaj numer indeksu: ")
        Classes.DailyStudent(name, surname, pesel, studentID)


start()
