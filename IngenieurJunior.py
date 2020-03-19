from Ingenieur import *

class IngenieurJunior(Ingenieur):
    def __init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail,nbhprojet,nbhgestion,nbanneeexp):
        Ingenieur.__init__(self,nom,prenom,salaire,identifiant,anneeEmbauche,nbjtravail,nbhprojet,nbhgestion)
        self.__nbanneeexp = nbanneeexp

    def Afficher(self):
        print(f"* [id={self._identifiant}] Nom et prénom : {self._nom} {self._prenom}, Salaire : {self._salaire}, Statut : IngenieurJunior, Année d'embauche : {self._anneeEmbauche}, Nombre de jour de travail : {self._nbjtravail}, Nombre d'heures de projet : {self._nbhprojet}, Nombre d'heures de gestion : {self._nbhgestion}, Nombre d'années d'expérience : {self.__nbanneeexp} ans")
