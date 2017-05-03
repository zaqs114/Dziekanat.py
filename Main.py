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


def edit_information_menu():
    choice = input("""  
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby edytować informacje o studentach.
        """)
    if choice == "0":
        start()
    if choice == "1":
        print("lol")
    if choice == "2":
        print("kappa")


def students_menu():
    choice=input("""
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


def add_student():
    print("dodawanie studenta")


start()
