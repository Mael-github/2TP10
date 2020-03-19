from Ingenieur import *

class IngenieurSenior(Ingenieur):
    def __init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail,nbhprojet,nbhgestion,resp):
        Ingenieur.__init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail,nbhprojet,nbhgestion)
        self.__responsabilite = resp

    def Afficher(self):
        print(f"* [id={self._identifiant}] Nom et prénom : {self._nom} {self._prenom}, Salaire : {self._salaire}, Statut : IngenieurSenior, Année d'embauche : {self._anneeEmbauche}, Nombre de jour de travail : {self._nbjtravail}, Nombre d'heures de projet : {self._nbhprojet}, Nombre d'heures de gestion : {self._nbhgestion}, Responsabilité : {self.__responsabilite}")

