import Classes
import os


def subjects_menu():
    choice = input("""Przedmioty.
            Wybierz 0 aby powrócić do poprzedniego menu.
            Wybierz 1 aby dodać przedmiot.
            Wybierz 2 aby usunąć przedmiot.
            """)
    if choice == "0":
        subject_write_to_file()
        os.system('cls')
        import Main
        Main.edit_information_menu()
    if choice == "1":
        os.system('cls')
        subjectName = input("Podaj nazwe przedmiotu:")
        subjectID = input("Podaj oznaczenie przedmiotu: ")
        Classes.Subjects.subjectList.append(Classes.Subjects(subjectName, subjectID))
        os.system('cls')
        print("Pomyślnie dodano przedmiot")
        print()
        subjects_menu()
    if choice == "2":
        os.system('cls')
        try:
            j = 1
            print("Usuwanie przedmiotu.")
            print()
            if not Classes.Subjects.subjectList:
                print("Nic tu nie ma!")
                choice = input("""Wybierz cokolwiek aby powrócić.
                """)
                os.system('cls')
                subjects_menu()

            for i in Classes.Subjects.subjectList:
                print(j, '. ',i)
                j += 1
            choice = int(input("""Wybierz pozycję którą chcesz usunąć.
            """))
            choice -= 1  # ponieważ liczymy od 0 a nie od 1
            Classes.Subjects.subjectList.pop(choice)
            os.system('cls')
            print("Pomyślnie usunięto przedmiot.")
            print()
            subjects_menu()
        except:
            os.system('cls')
            print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
            """)
            subjects_menu()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
            """)
        subjects_menu()


def show_students():
    for i in Classes.Subjects.subjectList:
        print(i)
    choice = int(input("""Wybierz 0 aby powrócić do poprzedniego menu.
    """))
    if choice == 0:
        import Main
        Main.show_base_menu()
    else:
        print("")


def subject_write_to_file():
    subjects = open("przedmioty.txt", "w")
    for i in Classes.Subjects.subjectList:
        subjects.write(str(i) + '\n')
    subjects.close()