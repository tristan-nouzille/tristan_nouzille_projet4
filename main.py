"""""""""""
Ceci est le code source pour le logiciel du tournoi d'Echecs local

"""""""""""

from controller.controller import Controller
from models.models import Joueur, Tournoi
from view.view import View


def main():
    
    view = View()
    controller = Controller(Joueur, Tournoi, view)
    controller.run() 
    
if __name__ == "__main__":
    main()







    






    






    