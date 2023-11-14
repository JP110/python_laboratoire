from laboratoire import *
from services import *
from menu import *
'''
Interface sur le labo avec menu textuel.
'''

""" ancienne partie du menu sans le module 
def afficher_menu():
    print('1- Enregistrer une arrivée')
    print('2- Enregistrer le départ d\'une personne.')
    print('3- Modifier le bureau d\'une personne')
    print('4- Changer le nom  d\'une personne')
    print('5- Présence d\'une personne')
    print('6- Obtenir le bureau d\'une personne')
    print('7- Liste de tous les personnels avec le bureau occupé')
    print('8- Liste de tous les personnels avec le bureau occupé dans une page HTML')
    print('0- Quitter')
 
def demander_choix():
    return input_natural("Votre choix: ") 

def traiter_choix(choix, labo):
    if choix == 1:
        gerer_arrivee(labo)
    elif choix == 2:
        nom = input("Nom ? ")
        reponse = est_presente(labo, nom)
        print('oui, présente' if reponse else 'non, inconnue') """
 
def gerer_arrivee(labo):
        try:
            nom = input("Nom ? ")
            bureau = input("Bureau ? ")
            enregistrer_arrivee(labo, nom, bureau)
        except PresentException:
            print("Impossible d'ajouter la persoone! Une personne portant ce nom est déjà présente dans le laboratoire.")

def gerer_depart(labo):
        try:
            nom = input("Nom de la personne quittant le laboratoire? ")
            enregistrer_depart(labo, nom)
        except AbsentException:
            print("Impossible de supprimer cette personne! Cette personne ne fait pas parti du laboratoire")

def gerer_modification_bureau(labo):
        try:
            nom = input("Nom ? ")
            bureau = input("Bureau ? ")
            modifier_bureau(labo, nom, bureau)
        except ArithmeticError:
            print("Impossible de modifier le bureau de cette personne! Cette personne ne fait pas parti du laboratoire.")


def gerer_modification_nom(labo):
        try:
            ancien_nom = input("Nom à modifier ? ")
            nouveau_nom = input("Nouveau nom? ")
            modifier_nom(labo, ancien_nom,nouveau_nom)
        except AbsentException:
            print("Impossible de modifier le nom cette personne! Cette personne ne fait pas parti du laboratoire")

def gerer_obtenir_bureau(labo):
    try:
        nom = input("Nom ? ")
        bureau(labo, nom)
    except AbsentException:
        print("Impossible d'otbenire le bureau de cette personne! Cette personne ne fait pas parti du laboratoire.")





def gerer_est_presente(labo): 
    nom = input("Nom ? ")
    reponse = est_presente(labo, nom)
    print('oui, présente' if reponse else 'non, inconnue')

def affichage_laboratoire_complet(labo):
      for nom, bureau in labo.items():
         print(f"{nom} : {bureau}")

""" def gerer_personnels_par_bureau(labo):
    affectations = personnels_par_bureau(labo)
    for bureau, noms in affectations.items():
         print(bureau)
         for nom in noms:
              print(f"- {nom}") """

def gerer_personnels_par_bureau_trié(labo):
    affectations = personnels_par_bureau_trié(labo)
    for bureau, noms in affectations.items():
         print(bureau)
         for nom in noms:
              print(f"- {nom}")
              
def creer_page_html(labo):
    mon_labo = personnels_par_bureau_trié(labo)
    # Commencer la construction de la page HTML
    page_html = "<html><body>"

    # Ajouter le titre
    page_html += "<h1>Personnels du laboratoire par bureau</h1>"

    # Ajouter un tableau dans la page hml
    page_html += "<table border='1'><tr><th>Bureau</th><th>Personnels</th></tr>"

    for bureau, noms in mon_labo.items():
        # Ajouter une entrée de liste pour chaque paire bureau, nom
        page_html += f"<tr><td>{bureau} </td><td>"
        page_html += f"{noms} "
        page_html += "</td></tr>"

    # Fermer les balises HTML
    page_html += "</ul></body></html>"

    # Écrire le contenu dans un fichier HTML
    with open('page.html', 'w') as fichier_html:
        fichier_html.write(page_html)

    print("Fichier HTML créé avec succès.")


def main():
    labo = laboratoire()
    menu_laboratoire = menu()
    ajout_categorie(menu_laboratoire, 1, "Enregistrer une arrivée", lambda: gerer_arrivee(labo))
    ajout_categorie(menu_laboratoire, 2, "Enregistrer le départ d\'une personne", lambda: gerer_depart(labo))
    ajout_categorie(menu_laboratoire, 3, "Modifier le bureau d\'une personne", lambda: gerer_modification_bureau(labo))
    ajout_categorie(menu_laboratoire, 4, "Changer le nom  d\'une personne", lambda: gerer_modification_nom(labo))
    ajout_categorie(menu_laboratoire, 5, "Présence d\'une personne?", lambda: gerer_est_presente(labo))
    ajout_categorie(menu_laboratoire, 6, "Obtenir le bureau d\'une personne", lambda: gerer_obtenir_bureau(labo))
    ajout_categorie(menu_laboratoire, 7, "Liste de tous les personnels avec le bureau occupé", lambda: gerer_personnels_par_bureau_trié(labo))
    ajout_categorie(menu_laboratoire, 8, "Liste de tous les personnels avec le bureau occupé dans une page HTML", lambda: creer_page_html(labo))
    ajout_categorie(menu_laboratoire, 0, "Quitter", lambda: quitter_menu())

    lancer_menu(menu_laboratoire)
    """     while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        quitter = choix == 0 """
    print("Aurevoir ...")
 
if __name__ == '__main__':
    main()