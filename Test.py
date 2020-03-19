from Multinationale import *
from Filiale import *
from Salarie import *
from Directeur import *
from Employe import *
from Ingenieur import *
from IngenieurJunior import *
from IngenieurSenior import *
from Administratif import *

maMulti = Multionationale ("RCAT","FRANCE")

FilTun = Filiale("RCAT-Tunisie","Tunisie",2008)
FilBel = Filiale("RCAT-Belgique","Belgique",2016)
FilMar = Filiale("RCAT-Maroc","Maroc",2012)
FilAng = Filiale("RCAT-Angleterre","Angleterre",2014)
maMulti.AjouterFiliale(FilTun)
maMulti.AjouterFiliale(FilBel)
maMulti.AjouterFiliale(FilMar)
maMulti.AjouterFiliale(FilAng)

directTuni = Directeur("Jenner","Kylie",10,1452,2017)
FilTun.AjouterSalarie(directTuni)

admiTuni = Administratif("Muscu","Karim",8,1414,2015,50,"chomage")
IngeSeniorTuni = IngenieurSenior("Jenner","Kris",7,1450,2013,60,70,90,"Nucléaire")
FilTun.AjouterSalarie(admiTuni)
FilTun.AjouterSalarie(IngeSeniorTuni)

admiBelg = Administratif("Elvis","Roméo",8,1454,2015,50,"Chocolat")
IngeJunBelg = IngenieurJunior("West","North",1,1450,2013,60,70,90,3)
FilBel.AjouterSalarie(admiBelg)
FilBel.AjouterSalarie(IngeJunBelg)

IngeSeniorMaroc = IngenieurSenior("LaSquale","Moha",7,1450,2013,60,70,90,"Détaille")
FilMar.AjouterSalarie(IngeSeniorMaroc)

#print("-----")
#maMulti.Afficher()
#print("-----")

#FilTun.SupprimerSalarie(admiTuni)
#print("-----")
#maMulti.Afficher()
#print("-----")

FilTun.SupprimerSalarie(IngeSeniorTuni)
FilBel.AjouterSalarie(IngeSeniorTuni)
print("-----")
maMulti.Afficher()
print("-----")
