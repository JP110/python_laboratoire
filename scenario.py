from laboratoire import *
import pytest
from ihm import *
def test_main():
   # labo = laboratoire()
    """ enregistrer_arrivee(labo, 'Xavier', 'F305')
    enregistrer_arrivee(labo, 'Marc', 'F305')
    enregistrer_arrivee(labo, 'CAtherine', 'F8885')
    print(labo)
    assert est_presente(labo, 'Xavier')
    assert est_presente(labo, 'Marc')
    assert not est_presente(labo, 'Aurélie')
    # assert bureau(labo, 'Xavier') == 'F305'
    enregistrer_depart(labo, 'Marc')
    # enregistrer_depart(labo, 'Aurélie')
    print(labo)
    enregistrer_arrivee(labo, 'Marc', 'F305')
    modifier_bureau(labo,'Marc','B506')
    assert labo['Marc']== 'B506'
    print(labo)
    modifier_nom(labo, 'Marc', 'Alain')
    print(labo)
    assert labo['Alain']== 'B506'
    assert bureau(labo, 'Xavier') == 'F305'
    enregistrer_arrivee(labo, 'Bobo', 'F305')
    #gerer_personnels_par_bureau_trié(labo)
    creer_page_html(labo) 
    """
   # save_to_json(labo, "testconsistence")
    #labo = load_from_json("labo.json")
    labo = load_from_csv("labo.csv")
    creer_page_html_labo(labo)
test_main()
