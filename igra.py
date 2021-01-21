print ("Solitaire")
print ("Tonio-Nina-Anđela-Mirna")
print("Naša igra")
class Karta(object):
  __karta_info = {1: ('as'),
                  2: ('dvica'),
                  3: ('trica'),
                  4: ('četvorka'),
                  5: ('petica'),
                  6: ('šestica'),
                  7: ('sedmica'),
                  8: ('osmica'),
                  9: ('devetka'),
                  10: ('desetka'),
                  11: ('dečko'),
                  12: ('dama'),
                  13: ('kralj')}
  __boje = ['pik','herc','karo', 'tref']
  
  @staticmethod 
  def brojevi():
    return Karta.__karta_info.keys()
  
  @staticmethod
  def boja():
    return list(Karta.__zogovi)
  
  def __init__(self, broj, boja, vidljiva=False):
    self.__broj=broj
    self.__boja=boja
    self.__vidljiva=vidljiva
  
  @property
  def broj(self):
    return self.__broj
  
  @property
  def boja(self):
    return self.__boja
  
  @property
  def naziv(self):
    return Karta.__karta_info[self.__broj][0]
  
  @property
  def vidljiva(self):
    return self.__vidljiva
  
  @vidljiva.setter
  def vidljiva(self,value):
    self.__vidljiva = value
   
  def __repr__(self):
    return self.__class__.__name__ + '(%r, %r, %r)' % (self.__broj, self.__boja, self.__vidljiva)
  
  def __str__(self):
    return self.naziv.title() + ' ' + self.zog
  
  @staticmethod
  def jeVeca(broj,kartaPrva,kartaDruga):
    if kartaPrva.broj==broj and kartaDruga==broj:
      return kartaPrva.broj>kartaDruga.broj
    elif kartaPrva.broj!=broj and kartaDruga.broj==broj:
      return False
    elif kartaPrva.broj==broj and kartaDruga.broj!=broj:
      return True
    elif kartaPrva.broj==kartaDruga.broj:
      return kartaPrva.broj>kartaDruga.broj
    return True
  
for boja in Karta.boje():
  for broj in Karta.brojevi():
    k=Karta(broj, boja)
    print ('%r %s' % (k, k))
    

class Spil(object):

    def __init__(self):
        self.__karte = []
        for boja in Karta.boje():
            for broj in Karta.brojevi():
                self.__karte.append(Karta(broj,boje))

    def __str__(self, red = 7, velicina = 18):
        return '\n'.join(''.join(str(karta).ljust(velicina, ' ') for karta in self.__karte[i:i+red]) for i in range(0, len(self.__karte), red)) + '\n'


    def dajKartu(self, broj_karata = 1):
        daneKarte = []
        while broj_karata > 0:
            daneKarte.append(self.__karte.pop())
            broj_karata -= 1
        return daneKarte

    def izvadiBoju(self):
        kartaBoje = self._karte.pop()
        self.__karte.insert(0, kartaBoje)
        return kartaBoje

    def promjesaj(self):
        import random
        random.shuffle(self.__karte)

    def imaKarata(self):
        return len(self.__karte) > 0

class Igrac(object):

    def __init__(self,ime):
        self.__ime = ime
        self.__karteZaSlaganje = []
        self.__karteDobivene = []

    @property
    def ime(self):
        return self.__ime

    @property
    def karteZaSlaganje(self):
        return self.__karteZaSlaganje

    @karteZaSlaganje.setter
    def karteZaSlaganje(self, value):
        self.__karteZaSlaganje = value

    def baciKartu(self, izbor):
        karta = self.__karteZaSlaganje.pop(izbor)
        return karta

    def uzmiKarteZaSlaganje(self, karte):
        self.__karteZaSlaganje += karte

    def uzmiKarteDobivene(self, karte):
        self.__karteDobivene += karte 

    def imaKarataZaSlaganje(self):
        return len(self.__karteZaSlaganje) > 0

    def bodovi(self):
        return sum(karta.bod for karta in self.__karteDobivene)

    def __str__(self):
        return "Igrač " + self.__ime
    
class PrikazIgre(object):
  def prikaziPocetakIgre(self):
    print("*" * 50)
    print("*" * 20 + "Solitaire" + "*" * 20)
    print("*" * 50)
    
  def unesiIgraca(self):
    while true:
        ime=input("Unesi ime: ")
        if ime.strip():
          print("*" * 50)
          return ime.strip()
  def prikaziBoju(self, kartaBoje):
    print("Solitaire je: " + str(kartaBoje))
    print("*" * 50)
    
  def izaberiKartuZaSlaganje(self, kartaZaSlaganje):
     text = ">>>baci kartu\n" + '\n'.join(' ' + str(i+1) + ') ' + str(karta) for i, karta in enumerate(kartaZaSlaganje)) + '\n>>>'
     while True:
        izbor = input(text)
        if izbor.isdigit() and int(izbor) >= 1 and int(izbor) <= len(kartaZaSlaganje):
            return int(izbor) - 1
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 
