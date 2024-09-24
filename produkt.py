

class Produkt:
  def __init__(self, id, mængde, pris):
    self.__id = id
    self.__mængde = mængde
    self.__pris = pris
  @property
  def id(self):
    return self.__id
  @property
  def mængde(self):
    return self.__mængde
  @property
  def pris(self):
    return self.__pris
  @mængde.setter
  def mængde(self, nyMængde):
    if(nyMængde < 0):
      print("Mængden skal være et positivt tal")
      return
    self.__mængde = nyMængde
  @pris.setter
  def pris(self, nyPris):
    if(nyPris < 0):
      print("prisen skal være et positivt tal")
      return
    self.__pris = nyPris
