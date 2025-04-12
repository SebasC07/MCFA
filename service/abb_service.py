from model.abb import ABB
from model.pet import Pet


class ABBService():
    def __init__(self):
        self.abb = ABB()
        # llenar ABB

        self.abb.add(Pet(id=7,name="fiona",age=11, race= "criollo", location= "barrancabermeja", gender="hembra"))
        firulais = Pet(id=2,name="firulais",age=5, race= "labrador", location="manizales", gender="macho")
        self.abb.add(firulais)