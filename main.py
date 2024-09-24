from lager import *

#Initialiser lager
lageret = Lager()

def main():
  print("Velkommen til Lageret!")
  print("Vælg hvad du vil gøre:")
  print(" 1.  Tilføj produkt til lager")
  print(" 2.  opdater produkt")
  print(" 3.  vis rapport over produkternes pris")
  menuValg = input("Skriv 1, 2 eller 3:")
  if(menuValg == "1"):
    tilføj()
  elif(menuValg == "2"):
    opdater()
  elif(menuValg == "3"):
    rapport()
  else:
    print("vælg 1, 2 eller 3")
    main()

def tilføj():
  nyId = input("id: ")
  nyMængde = input("mængde: ")
  nyPris = input("pris: ")
  lageret.tilføj(nyId, nyMængde, nyPris)
  main()

def opdater():
  idIn = input("id: ")
  if(not lageret.tjekId(idIn)):
    print("produktet kunne ikke findes")
    main()
  nyMængde = input("Nye mængde: ")
  nyPris = input("Ny pris: ")
  lageret.opdater(idIn, nyMængde, nyPris)
  main()

def rapport():
  lageret.rapport()
  main()


main()