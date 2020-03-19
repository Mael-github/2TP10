class Multionationale:
    def __init__(self,nom,pays):
        self.__nom = nom
        self.__pays = pays
        self.__filiale = []

    def AjouterFiliale(self,filiale):
        self.__filiale.append(filiale)

    def Afficher(self):
        print(f"- La multinationale {self.__nom} est composée de {len(self.__filiale)} filiales. Son pays d'origine est : {self.__pays}.")

        dateplusvielle = 999999999999999999999999999999999
        counter = 0
        numerofiliale = 0
        nombretotal = 0
        for i in self.__filiale:
            datefiliale = i.gettdate()
            nombretotal = nombretotal + (self.__filiale[counter]).gettnombresalarie()
            if datefiliale < dateplusvielle :
                dateplusvielle = datefiliale
                numerofiliale = counter
            counter = counter + 1
        filialelaplusvielle = (self.__filiale[numerofiliale]).gettnom()
        nombredemploye = (self.__filiale[numerofiliale]).gettnombresalarie()

        print(f"- La filiale la plus ancienne de cette multinationale est {filialelaplusvielle}: . Elle est composée de {nombredemploye} salariés.")
        print(f"- {self.__nom} est composée de {nombretotal} salariés :")
        for f in self.__filiale:
            f.Afficher()
