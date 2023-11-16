class SignError(Exception):
    pass
 
 
def natural(chaine):
    """
    Retourner l'entier naturel qui correspond à chaine.
 
    Paramètres
        chaine: une chaîne de caractères
 
    Retour
        L'entier naturel qui correspond à chaine
 
    Exception
        ValueError si chaine n'est pas en entier
        SignError si l'entier est négatif
    """
    assert isinstance(chaine, str)
 
    entier = int(chaine)
    if entier < 0:
        raise SignError("Non positiv integer: " + chaine)
    return entier
 
 
def input_natural(consigne):
    '''
    Réaliser une saisir robuste d'un entier naturel.
    La consigne est affichée avant chaque saisie.
    '''
    while True:
        try:
            return natural(input(consigne))
        except ValueError:
            print("Un entier est attendu.")
        except SignError:
            print("Un entier positif est attendu.")
 
if __name__ == "__main__":
    age = input_natural("Age ? ")
    print("Age =", age)