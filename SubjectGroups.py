import Classes
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


def add_subject_group():
        print("Dodawanie grupy przedmiotowej.")
        j = 1
        for i in Classes.Subjects.subjectList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz przedmiot dla którego chcesz utworzyć nową grupę..
                    """))
        choice -= 1
        subjectGroupName = Classes.Subjects.subjectList[choice].Classes.Subjects.__getattribute__(na)
        print(subjectGroupName)



        choice = input("""Dodawanie grupy przedmiotowej.
        Wybierz 1, jeśli ma to być grupa studiów dziennych.
        Wybierz 2, jeśli ma to być grupa studiów zaocznych.
        Wybierz 0 aby powrócić do poprzedniego menu.
        """)
        if choice == 0:
            os.system('cls')
            subject_groups_menu()
        if choice == 1:
            os.system('cls')
            studiesType = "Dzienne"

            choice -= 1  # ponieważ liczymy od 0 a nie od 1
            Classes.DailyStudent.dailyStudentList.pop(choice)
            os.system('cls')
            print("Pomyślnie usunięto studenta.")
            print()
            delete_student()
        Classes.SubjectGroups.subjectGroupsList.append(
            Classes.SubjectGroups(subjectGroupName, subjectGroupID, studiesType, teacherName, nameOfStudents))
        os.system('cls')
        print("Pomyślnie dodano przedmiot")
        print()
        subject_groups_menu()


def delete_subject_group():
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
