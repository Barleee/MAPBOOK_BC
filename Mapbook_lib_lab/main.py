# Definicja prostej struktury danych obejmującej przykładowego użytkownika
from Mapbook_lib_lab.controller import read_users, add_user, remove_user, update_user_post, update_user, get_user_map
from Mapbook_lib_lab.model import users

def main():


    while True:
        print("===========MENU===========")
        print("0 - zakończ program")
        print("1 - wyświetl znajomych")
        print("2 - dodanie znajomego")
        print("3 - usuń znajomego")
        print("4 - aktualizacja znajomego")
        print("5 - aktualizacja posta")
        print("6 - mapa lokalizacji znajomych")
        choice=input("Wybierz opcje menu:  ")
        print(f"Wybrano opcje {choice}")
        if choice == "0":
            break

        if choice == "1":
            read_users(users)

        if choice == "2":
            add_user(users)

        if choice == "3":
            remove_user(users)

        if choice == "4":
            update_user(users)

        if choice == "5":
            update_user_post(users)
        if choice == "6":
            get_user_map(users)

if __name__ == "__main__":
    main()
