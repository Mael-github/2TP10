from Salarie import *

class Directeur(Salarie):
    def __init__(self,nom,prenom,salaire,identifiant,anneeNom):
        Salarie.__init__(self,nom,prenom,salaire,identifiant)
        self.__anneeNomination = anneeNom

    def Afficher(self):
        print(f"* [id={self._identifiant}] Nom et prénom : {self._nom} {self._prenom}, Salaire : {self._salaire}, Statut : Directeur, Année de nomination : {self.__anneeNomination}")

