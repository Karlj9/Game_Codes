import tkinter as tk
from tkinter import ttk
import string
la_liste_au_code_cache = []                                                     # Dans cette liste je placerai le mot caché
le_mot_cache = "Chien"                                                          # Le mot de passe va être caché celon la methode du code cesar
cle=24                                                                          # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)
acrypter=le_mot_cache.upper()
lg=len(acrypter)
MessageCrypte=""
cpt = 10
cpt2 =0

for i in range(lg):
    if acrypter[i]==' ':
        MessageCrypte+=' '
    else:
        asc=ord(acrypter[i])+cle
        MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

while (cpt2!=cpt):
    print ("nombre de tentative = ", 10 - cpt2)
    if cpt2 == 0:
        print ("Premier indice : quadrupède")                                   # Renvoie un premier indice à l'utilisteur
    elif cpt2 ==1:
        print ("Deuxieme indice : Poilu")                                       # Renvoie un deuxième indice à l'utilisteur
    elif cpt2 ==2:              
        print ("Troisieme indice : Maison")                                     # Renvoie un troisième indice à l'utilisateur

    le_code = input ("entrez le mot de passe ('aide' pour un autre indice): ")  # L'utilistateur entre un mot ou un nombre
    la_liste_au_code_cache.append(le_code)                                      # Ce que l'utilisateur à rentré je le met dans ma liste
    for j in la_liste_au_code_cache:
        if j == "aide":
            print ("l'indice est : ", MessageCrypte)
        elif j == "Chien":
            print("!!!! BIEN JOUÉ !!!! (❍ᴥ❍ʋ)")
            cpt2 = 10
        elif j == "Chat":
            print("vous n'êtes pas loin de la solution")
        elif j != "Chat" or "Chien" or "aide":
            print('LOOSER LOOSER CODER SUCKER ╭∩╮ (︶︿︶) ╭∩╮')
    if cpt2 == 10:
        break
    cpt2 += 1

with open('animaux.txt') as file:
    lignes = file.readlines()
    for les_mots_de_la_liste in lignes:
        print("_____________________")
        print(les_mots_de_la_liste)
        print(le_mot_cache)
        print("_____________________")
        if les_mots_de_la_liste == "Chien":
            print("le mot est dans la liste")
