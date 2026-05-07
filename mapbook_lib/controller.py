
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
            user.data.remove(user)


def update_user(users_data:list)->None:
    user_to_update = input("Podaj imię znajomego do updatu  ")
    for user in users_data:
        if user["Name"] == user_to_update:
            user["Name"] ==(input("Podaj nowe imię użytkownika "),
            user["Location"] ==(input("Podaj nową lokalizacje "),
            user["Location"] ==(input("Podaj nowe lokalizacje ")
def update_user_post(users_data:list)->None:
    user_to_update = input("Podaj imię znajomego do updatu  ")
    for user in users_data:
        if user["Name"] == user_to_update:
            user ["Posts"].append(input("Co słychać  "))

