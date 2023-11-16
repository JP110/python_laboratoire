import json
from pathlib import Path  # Utilisé pour travailler avec les chemins de fichiers de manière plus propre
import csv
# ... (le reste de votre code)

def save_to_json(labo, filename):
    """Enregistre les données du laboratoire au format JSON.

    Args:
        labo (dict): Laboratoire à enregistrer
        filename (str): Nom du fichier JSON de sortie
    """
    with open(filename, 'w') as json_file:
        json.dump(labo, json_file, indent=4)

def load_from_json(labo,filename):
    """Charge les données du laboratoire depuis un fichier JSON.

    Args:
        filename (str): Nom du fichier JSON d'entrée

    Returns:
        dict: Laboratoire chargé depuis le fichier JSON
    """
    if Path(filename).exists():  # Vérifie si le fichier existe avant de tenter de le charger
        with open(filename, 'r') as json_file:
            loaded_labo = json.load(json_file)
            labo.clear()
            labo.update(loaded_labo)
    else:
        print(f"Le fichier {filename} n'existe pas. Création d'un nouveau laboratoire.")
        return {}


def load_from_csv(labo,filename):
    """Charge les données du laboratoire depuis un fichier CSV.

    Args:
        filename (str): Nom du fichier CSV d'entrée

    Returns:
        dict: Laboratoire chargé depuis le fichier CSV
    """
    if Path(filename).exists():  # Vérifie si le fichier existe avant de tenter de le charger
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            loaded_labo = {}
            for ligne in reader:
                loaded_labo[ligne['Nom']] = ligne['Bureau']
        labo.update(loaded_labo)
    else:
        print(f"Le fichier {filename} n'existe pas. Création d'un nouveau laboratoire.")
        return {}



'''
Les opérations sur le laboratoire sans interactions avec l'utilisateur.
Pas de input, pas de print.
Backend.
Partie réutilisable entre les différentes IHM.
python labo_cmd.py add Xavier F305
'''

# Définir ce qu'est un laboratoire ? Quel type ?
 
# Réponse : dictionnaire, clé = personne, valeur = bureau
 
'''
Evolution possible :
    labo = {
        'bureaux' : {
            'F305': 4,
            'F307': 2,
        },
        'affectations': {
            'Xavier': 'F305',
        }
 
    }
'''

 # Les opérations qui permettent de manipuler les données du labo.
 
def laboratoire():
    return {}
 
def enregistrer_arrivee(labo, nom, bureau):
    """Permet d'enregistrer l'arrivée d'une nouvelle personne dans le laboratoire

    Args:
        labo (dict): laboratoire dans lequel on veut ajouter la personne
        nom (string): nom de la personne à enregistrer
        bureau (string): bureau dans lequel on veut enregistrer nom

    Raises:
        PresentException: Levé si nom  est déjà présent dans labo
    """
    if nom in labo:
        raise PresentException
    labo[nom] = bureau
    
def enregistrer_depart(labo, nom):
    """Permet d'enregistrer le départ d'une personne présente dans le laboratoire

    Args:
        labo (dict): laboratoire dans lequel on veut supprimer la personne
        nom (string):  nom de la personne à supprimer de labo

    Raises:
        AbsentException: Levé si nom n'est pas présent dans labo
    """
    if not nom in labo:
        raise AbsentException
    del labo[nom]


def modifier_bureau(labo, nom, bureau):
    """Modifie le bureau d'une personne présente dans le laboratoire

    Args:
        labo (dict): laboratoire
        nom (string): nom de la personne que l'on souhaite modifier de bureau
        bureau (string): nouveau bureau d'affectation de nom

    Raises:
        AbsentException:  Levé si nom n'est pas présent dans labo
    """
    if not nom in labo:
        raise AbsentException
    labo[nom] = bureau
 

def modifier_nom(labo, ancien_nom, nouveau_nom):
    """Modifie le nom d'une persone présente dans le laboratoire

    Args:
        labo (dict): laboratoire
        ancien_nom (string): Ancien nom de la personne que l'on souhaite modifiier
        nouveau_nom (string): Nouveau nom de la personne

    Raises:
        AbsentException:  Levé si nom n'est pas présent dans labo
    """
    if not ancien_nom in labo:
        raise AbsentException
    labo[nouveau_nom] = labo.pop(ancien_nom)


def est_presente(labo, nom):
    """Test si une personne est présente dans le laboratoire par son nom

    Args:
        labo (dict): laboratoire
        nom (string): nom de la personne qu'on veut tester

    Returns:
        bool: vrai si la personne est présente dans le laboratoire sinon false
    """
    return nom in labo

def bureau(labo, nom):
    """Retourne le bureau d'une personne

    Args:
        labo (dict): laboratoire
        nom (string): nom de la personne 

    Raises:
        AbsentException:  Levé si nom n'est pas présent dans labo

    Returns:
        string: Retourne le bureau d'une personne
    """
    if not nom in labo:
        raise AbsentException
    return labo[nom]
    
def personnels_par_bureau(labo):
    """Affiche tous la liste de tous les personnels groupé par bureau

    Args:
        labo (dict): laboratoire

    Returns:
        dict: retourne un dictionnaire avec comme clé les bureau et en valeurs les différentes personne présente dans ces bureaux
    """
    affectation_labo = {}
    for cle, valeur in labo.items():
        # Si la valeur n'est pas déjà une clé dans le dictionnaired'affectation , l'ajouter avec une liste vide
        affectation_labo.setdefault(valeur, [])

        # Ajouter la clé à la liste correspondante dans le  dictionnaire d'affectation
        affectation_labo[valeur].append(cle)
    return affectation_labo   

def personnels_par_bureau_trié(labo):
    """Affiche tous la liste de tous les personnels groupé par bureau classé par odre alphaébique (clé et valeurs)

    Returns:
        dict: retourne un dictionnaire trié par odre alphabétique (clé et valeurs) avec comme clé les bureau et en valeurs les différentes personne présente dans ces bureaux
    """
    affectation_labo = personnels_par_bureau(labo)
    affectation_labo_triees = sorted(affectation_labo.keys())
    for bureau in affectation_labo_triees:
        affectation_labo[bureau] = sorted(affectation_labo.pop(bureau))
    return affectation_labo   




 

#Généralise les exceptions du laboratoire
class LaboException(Exception):
    pass
class AbsentException(LaboException):
    pass
class PresentException(LaboException):
    pass
