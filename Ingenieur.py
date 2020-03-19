from Employe import *

class Ingenieur(Employe):
    def __init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail,nbhprojet,nbhgestion):
        Employe.__init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail)
        self._nbhprojet = nbhprojet
        self._nbhgestion = nbhgestion

    def Afficher(self):
        pass
