# # interakcje z obiektami/tabelami/itp Dodanie do innego podfolderu dodanie from *
# from tkinter import *
# from main import *
#
# users:list = []
#
# class User:
#     def __init__(self, imie: str, nazwisko:str, posty: int, lokalizacja:str):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.posty = posty
#         self.lokalizacja = lokalizacja
#
# def show_user()->None:
#     listbox_lista_obiektow.delete(0, END)
#     for idx, user in enumerate(users):
#         listbox_lista_obiektow.insert(END, user.imie)
#
# def remove_user()->None:
#     i = listbox_lista_obiektow.index(ACTIVE)
#     users.pop(i)
#
#     show_user()
#
# def show_user_details()->None:
#     i = listbox_lista_obiektow.index(ACTIVE)
#     imie = users[i].imie
#     nazwisko = users[i].nazwisko
#     posty = users[i].posty
#     lokalizacja = users[i].lokalizacja
#
#     label_imie_szczegoly_obiektu_wartosc.config(text=imie)
#     label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
#     label_liczba_postow_obiektu_wartosc.config(text=posty)
#     label_lokalizacja_obiektu_wartosc.config(text=lokalizacja)
#
# def edit_user()->None:
#     i = listbox_lista_obiektow.index(ACTIVE)
#     imie = users[i].imie
#     nazwisko = users[i].nazwisko
#     posty = users[i].posty
#     lokalizacja = users[i].lokalizacja
#
#     entry_imie.inster(0,imie)
#     entry_nazwisko.insert(0, nazwisko)
#     entry_liczba_postow.insert(0, posty)
#     entry_lokalizacja.insert(0, lokalizacja)
#
#     button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda:update_user(i) )
#     show_user()
#
# def update_user(i):
#     users[i].imie=entry_imie.get()
#     users[i].nazwisko=entry_nazwisko.get()
#     users[i].possty = entry_liczba_postow.get()
#     users[i].lokalizacja=entry_lokalizacja.get()
#
#     button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=add_user)
#
# def add_user():
#     name = entry_imie.get()
#     surname = entry_nazwisko.get()
#     posts = entry_liczba_postow.get()
#     localization = entry_lokalizacja.get()
#
#     new_users = User(imie=name, nazwisko=surname, posty=int(posts), lokalizacja=localization)
#     users.append(new_users)
#     entry_imie.delete(0, END)
#     entry_nazwisko.delete(0, END)
#     entry_liczba_postow.delete(0, END)
#     entry_lokalizacja.delete(0, END)
#
#     entry_imie.focus()
#
#     show_user()

from tkinter import *
import tkinter
import tkintermapview

users:list = []

class User:
    def __init__(self, imie: str, nazwisko: str, posty: int, lokalizacja: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.lokalizacja = lokalizacja

def show_users()-> None:
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user.imie)

def remove_user()-> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    users.pop(i)
    show_users()

def show_user_details():
    i = listbox_lista_obiektow.index(ACTIVE)
    imie = users[i].imie
    nazwisko = users[i].nazwisko
    posty = users[i].posty
    lokalizacja = users[i].lokalizacja

    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    label_liczba_postow_szczegoly_obiektu_wartosc.config(text=posty)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)


def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    imie = users[i].imie
    nazwisko = users[i].nazwisko
    posty = users[i].posty
    lokalizacja = users[i].lokalizacja

    entry_imie.insert(0, imie)
    entry_nazwisko.insert(0, nazwisko)
    entry_liczba_postow.insert(0, posty)
    entry_lokalizacja.insert(0, lokalizacja)


    button_dodaj_uzytkownika.config(text= "Zapisz zmiany", command=lambda: update_user(i))

def update_user(i):
    users[i].imie = entry_imie.get()
    users[i].nazwisko = entry_nazwisko.get()
    users[i].posty = entry_liczba_postow.get()
    users[i].location = entry_lokalizacja.get()

    button_dodaj_uzytkownika.config(text= "Dodaj uzytkownika", command=add_user)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.focus()
    show_users()





def add_user():
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    posts = entry_liczba_postow.get()
    lokalizacja = entry_lokalizacja.get()

    # print(name, surname, posts, lokalizacja)
    new_user = User(imie=name, nazwisko=surname, posty=int(posts), lokalizacja=lokalizacja)
    users.append(new_user)
    # print(users)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.focus()
    show_users()














root = Tk()

root.title("Mapbook_AB")
root.geometry("1024x760")


# FRAME
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

# RAMKA LISTA OBIEKTOW
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista znajomych: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)

button_pokaz_szczegoly_obiektu = Button(ramka_lista_obiektow, text="Pokaz szczegoly", command = show_user_details)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usun", command=remove_user)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj", command = edit_user)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_imie = Label(ramka_formularz, text="Imię: ")
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_liczba_postow = Label(ramka_formularz, text="Liczba postow: ")
label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")

label_formularz.grid(row=0, column=0)
label_imie.grid(row=1, column=0)
label_nazwisko.grid(row=2, column=0)
label_liczba_postow.grid(row=3, column=0)
label_lokalizacja.grid(row=4, column=0)


entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_liczba_postow = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_liczba_postow.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text = "Dodaj użytkownika", command = add_user)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# SZCZEGOLY OBIEKTU

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Szczegóły użytkownika")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Imię: ")
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Nazwisko: ")
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_liczba_postow_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Liczba postów: ")
label_liczba_postow_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Lokalizacja: ")
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")



label_szczegoly_obiektu.grid(row=0, column=0)
label_imie_szczegoly_obiektu.grid(row=1, column=0)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_liczba_postow_szczegoly_obiektu.grid(row=1, column=4)
label_liczba_postow_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)


#















root.mainloop()