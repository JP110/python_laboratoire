from services import input_natural

quitter = False

def menu():
    return {}

def ajout_categorie(menu, categorie, descriptif, action):
    menu[categorie] = [descriptif, action]

def affichage_menu(menu: dict):
    for numero, categorie in menu.items():
        print(f"{numero}- {categorie[0]}")

def choix_utilisateur(menu: dict):
    while True:
        try:
            choix = int(input_natural("Votre choix: "))
            if choix in menu.keys():
                return choix
            else:
                print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro.")

def quitter_menu():
     global quitter 
     quitter = True

def lancer_menu(menu):
    global quitter 
    while not quitter:
        affichage_menu(menu)
        choice = choix_utilisateur(menu)
        categorie_choisi = menu[choice][1]
        if categorie_choisi == quitter_menu:
            continue
        categorie_choisi()
        print()
