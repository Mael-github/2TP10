from Multinationale import *

class Filiale(Multionationale):
    def __init__(self,nom,pays,date):
        self.__nom = nom
        self.__pays = pays
        self.__date = date
        self.__salarie = []

    def AjouterSalarie(self,salarie):
        self.__salarie.append(salarie)

    def SupprimerSalarie(self,salarie):
        self.__salarie.remove(salarie)

    def gettdate(self):
        return self.__date
    def gettnom(self):
        return self.__nom
    def gettpays(self):
        return self.__pays
    def gettsalarie(self):
        return self.__salarie
    def gettnombresalarie(self):
        return len(self.__salarie)

    def Afficher(self):
        for f in self.__salarie:
            f.Afficher()
            print(f"Site : {self.__pays}")
