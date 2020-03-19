from Employe import *

class Administratif(Employe):
    def __init__(self,nom,prenom,salaire,identifiant,anneeEm,nbjtravail,service):
        Employe.__init__(self,nom,prenom,salaire,identifiant,anneeEm,nbjtravail)
        self.__service = service

    def Afficher(self):
        print(f"* [id={self._identifiant}] Nom et prénom : {self._nom} {self._prenom}, Salaire : {self._salaire}, Statut : Administratif, Année d'embauche : {self._anneeEmbauche}, Nombre de jour de travail : {self._nbjtravail}, Service : {self.__service}")

