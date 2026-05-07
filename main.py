# Definicja prostej struktury danych obejmującej przykładowego użytkownika

users= [
    {"Name":"Artur","Location": "Łomża", "Posts": ["Sprzedam Mercedessa","Kupię skrzynie biegów","ratunku co robić po wypadku"]},
    {"Name":"Daniel","Location": "Legionowo", "Posts": ["Mój kod nie działa"]},
    {"Name":"Kamil","Location": "ciechanów", "Posts": ["Czy ktoś zrobił sprwozdanie z ppytch"]},
]


def read_users(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user["Name"]}, z miejscowośći {user["Location"]}, zamieścił post {user["Posts"][-1]}")
read_users(users)

def add_user(users_data:list)->None:
    users_data.append({"Name":input("Podaj imię  "),"Location":input("Twoja Lokalizacja  "), "Posts":input("Dołączono do znajomych  ")})

def remove_user(users_data:list)->None:
    user_to_remove = input("Podaj imię znajomego do usunięcia  ")
    for user in users_data:
        if user["Name"] == user_to_remove:
            users.remove(user)


def update_user(users_data:list)->None:
    user_to_update = input("Podaj imię znajomego do updatu  ")
    for user in users_data:
        if user["Name"] == user_to_update:
            user["Name"] ==(input("Podaj nowe imię użytkownika "),
            user["Location"] ==(input("Podaj nową lokalizacje ")

def update_user_post(users_data:list)->None:
    user_to_update = input("Podaj imię znajomego do updatu  ")
    for user in users_data:
        if user["Name"] == user_to_update:
            user ["Posts"].append(input("Co słychać  "))


while True:
    print("===========MENU===========")
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodanie znajomego")
    print("3 - usuń znajomego")
    print("4 - aktualizacja znajomego")
    print("5 - aktualizacja posta")
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