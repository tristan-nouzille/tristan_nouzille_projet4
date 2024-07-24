"""""""""""
Ceci est le code source pour le logiciel du tournoi d'Echecs local

"""""""""""

from controller.controller import Controller
from view.view import View
from models.models import Joueur, Tournoi, Tour, Match
from datetime import datetime

def main():
    model = Joueur, Tournoi, Tour, Match  # Initialisez votre modèle avec les classes
    view = View()  # Initialisez votre vue
    controller = Controller(model, view)  # Passez le modèle et la vue au contrôleur
    controller.run()

if __name__ == '__main__':
    main()






    






    






    