from Salarie import *

class Employe(Salarie):
     def __init__(self,nom,prenom,salaire,identifiant,anneeEm,nbjtravail):
        Salarie.__init__(self,nom,prenom,salaire,identifiant)
        self._anneeEmbauche = anneeEm
        self._nbjtravail = nbjtravail

     def Afficher(self):
        pass
