from produkt import *

class Lager:
  def __init__(self):
    self.__produkter = []
  def tilføj(self, nyId, nyMængde, nyPris):
    if(self.tjekId(nyId)):
      print("vælg ny Id, Id er allerede taget")
      return
    try: 
      self.__produkter.append(Produkt(nyId, int(nyMængde), int(nyPris)))
      print(f"produkt med id: {nyId}, mængde: {nyMængde} og pris: {nyPris} er tilføjet")
    except:
      print("Pris og mængden skal være tal")
  def tjekId(self, id):
    for produkt in self.__produkter:
      if(produkt.id == id):
        return True
    return False
  def opdater(self, id, nyMængde, nyPris):
    for produkt in self.__produkter:
      if(produkt.id == id):
        try:
          produkt.mængde = int(nyMængde)
          produkt.pris = int(nyPris)
          print(f"produkt med id: {id} har ny mængde: {nyMængde} og ny pris: {nyPris}")
          return
        except:
          print("Pris og mængden skal være tal")
          return
    print("desvære kunne produktet ikke findes")
  def rapport(self):
    total = 0
    for produkt in self.__produkter:
      total += produkt.pris*produkt.mængde
    print(f"Den samlede værdi af alle produkter i lageret er {total} DKK")