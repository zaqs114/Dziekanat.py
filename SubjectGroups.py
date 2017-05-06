import Classes
import Main
import os

def subject_groups_menu():
    choice = input("""Grupy przediotowe.
                Wybierz 0 aby powrócić do poprzedniego menu.
                Wybierz 1 aby dodać grupe przedmiotową.
                Wybierz 2 aby usunąć grupę przedmiotową.
                """)
    if choice == "0":
        subject_group_write_to_file()
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        subjectGroupName = input("Podaj nazwe przedmiotu:")
        studiesType = input("Podaj rodzaj studiów: ")
        subjectGroupID = input("Podaj oznaczenie grupy")
        teacherName = input ("Imię i nazwisko nauczyciela")
        nameOfStudents = input("Wprowadź imiona studentów")
        Classes.SubjectGroups.subjectGroupsList.append(Classes.SubjectGroups(subjectGroupName, subjectGroupID, studiesType, teacherName, nameOfStudents))
        os.system('cls')
        print("Pomyślnie dodano przedmiot")
        print()
        subject_groups_menu()
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
                subject_groups_menu()

            for i in Classes.Subjects.subjectList:
                print(j, '. ', i)
                j += 1
            choice = int(input("""Wybierz pozycję którą chcesz usunąć.
                """))
            choice -= 1  # ponieważ liczymy od 0 a nie od 1
            Classes.Subjects.subjectList.pop(choice)
            os.system('cls')
            print("Pomyślnie usunięto przedmiot.")
            print()
            subject_groups_menu()
        except:
            os.system('cls')
            print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
                """)
            subject_groups_menu()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
                """)
        subject_groups_menu()