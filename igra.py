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
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
