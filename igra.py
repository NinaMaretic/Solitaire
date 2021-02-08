import random
BREAK_STRING = "-------------------------------------------------------------------"
class Prikaz(object):

    def __init__(self): 
        pass
    def prikaziPocetakIgre(self):
        print("#"*50)
        print("#"*19 +" BATTLESHIP " + "#"*19)
        print("#"*50)

    def unesiIgraca(self):
        while True:
            ime = input("\nUnesi igraca ")
            if ime.strip():
                print("#"*50+"\n\n")
                return ime
                
class Karta():
	karta_ime = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",
					8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}

	def __init__(self, value, boja):
		self.ime = self.karta_ime[value]
		self.boja = boja
		self.naslov = "%s%s" % (self.ime, self.boja)
		self.value = value

	def Ispod(self, karta):
		return self.value == (karta.value - 1)

	def SuprotnaBoja(self, karta):
		if self.boja == "tref" or self.boja == "pik":
			return karta.boja == "herz" or karta.boja == "karo"
		else:
			return karta.boja == "pik" or karta.boja == "tref"

	def Slaganje(self, karta):
		if karta.Ispod(self) and karta.SuprotnaBoja(self):
			return True
		else:
			return False

	def __str__(self):
		return self.naslov

class Spil():
	nepromijesani_spil = [Karta(karta, boja) for karta in range(1, 14) for boja in ["tref", "karo", "herz", "pik"]]

	def __init__(self, broj_spil=1):
		self.spil = self.nepromijesani_spil * broj_spil
		random.shuffle(self.spil)

	def okreni_kartu(self):
		return self.spil.pop()

	def podijeli_karte(self, broj_spil):
		return [self.spil.pop() for x in range(0, broj_spil)]

	def __str__(self):
		return str(self.spil)

		
class Tablica():
	

	def __init__(self, karta_lista):
		self.neokrenuta = {x: karta_lista[x] for x in range(7)}
		self.okrenuta = {x: [self.neokrenuta[x].pop()] for x in range(7)}

	def okreni_kartu(self, stupac):
		
		if len(self.neokrenuta[stupac]) > 0:
			self.okrenuta[stupac].append(self.neokrenuta[stupac].pop())

	def duljina_skupa(self):
		
		return max([len(self.okrenuta[x]) + len(self.neokrenuta[x]) for x in range(7)])

	def dodajKarte(self, karte, stup):
		
		stup_karte = self.okrenuta[stup]
		if len(stup_karte) == 0 and karte[0].value == 13:
			stup_karte.extend(karte)
			return True
		elif len(stup_karte) > 0 and stup_karte[-1].Slaganje(karte[0]):
			stup_karte.extend(karte)
			return True
		else:
			return False

	def izTab_uTab(self, c1, c2):
		
		c1_karte = self.okrenuta[c1]

		for index in range(len(c1_karte)):
			if self.dodajKarte(c1_karte[index:], c2):
				self.okrenuta[c1] = c1_karte[0:index]
				if index == 0:
					self.okreni_kartu(c1)
				return True
		return False

	def izTab_uKucu(self, kuca, stup):
		
		stup_karte = self.okrenuta[stup]
		if len(stup_karte) == 0:
			return False

		if kuca.dodajKartu(stup_karte[-1]):
			stup_karte.pop()
			if len(stup_karte) == 0:
				self.okreni_kartu(stup)
			return True
		else:
			return False

	def izOtp_uTab(self, otp_skup, stupac):
		
		if len(otp_skup.otp)==0:
			return False
		karta = otp_skup.otp[-1]
		if self.dodajKarte([karta], stupac):
			otp_skup.pop_otp_karta()
			return True
		else:
			return False

class Pricuva():
	
	def __init__(self, karte):
		self.spil = karte
		self.otp = []

	def izOtp_uPric(self):
		
		if len(self.spil) + len(self.otp) == 0:
			print("Nema karata u pricuvi.")
			return False

		if len(self.spil) == 0:
			self.otp.reverse()
			self.spil = self.otp.copy()
			self.otp.clear()

		self.otp.append(self.spil.pop())
		return True

	def pop_otp_karta(self):
		
		if len(self.otp) > 0:
			return self.otp.pop()

	def getOtp(self):
		
		if len(self.otp) > 0:
			return self.otp[-1]
		else:
			return "prazno"

	def getPricuva(self):
		
		if len(self.spil) > 0:
			return str(len(self.spil)) + " karta(e)"
		else:
			return "prazno"

class Kuca():

	def __init__(self):
		self.skup_kuca = {"tref":[], "herz":[], "pik":[], "karo":[]}

	def dodajKartu(self, karta):

		skup = self.skup_kuca[karta.boja]
		if (len(skup) == 0 and karta.value == 1):
			skup.append(karta)
			return True
		elif(len(skup)+1==karta.value):
			skup.append(karta)
			return True
		else:
			return False
	def getGornjaKarta(self, boja):
		
		skup = self.skup_kuca[boja]
		if len(skup) == 0:
			return boja[0].upper()
		else:
			return self.skup_kuca[boja][-1]

	def pobjeda(self):
		
		for boja, skup in self.skup_kuca.items():
			if len(skup) == 0:
				return False
			karta = skup[-1]
			if karta.value != 13:
				return False
		return True

def Naredbe():
	
	print("Podržane naredbe: ")
	print("\tmv - pomakni kartu iz pricuve u otpad")
	print("\tok - pomakni kartu iz otpada u kucu")
	print("\tot #T - pomakni kartu iz otpada u tablicu")
	print("\ttk #T - pomakni kartu iz tablice u kucu")
	print("\ttt #T1 #T2 - pomakni kartu iz jednog stupca u drugi")
	print("\tp - pomoć")
	print("\tq - quit")
	print("\t*NAPOMENA: Herz/karo su crvene karte. Pik/tref su crne.")

def ispisiTablicu(tablica, kuca, pricuva):
	
	print(BREAK_STRING)
	print("Otpad \t Pricuva \t\t\t\t Temelj")
	print("{}\t{}\t\t{}\t{}\t{}\t{}".format(pricuva.getOtp(), pricuva.getPricuva(), 
		kuca.getGornjaKarta("tref"), kuca.getGornjaKarta("herz"), 
		kuca.getGornjaKarta("pik"), kuca.getGornjaKarta("karo")))
	print("\nTablica\n\t1\t2\t3\t4\t5\t6\t7\n")
	
	for x in range(tablica.duljina_skupa()):
		print_str = ""
		for stupac in range(7):
			skrivene_karte = tablica.neokrenuta[stupac]
			prikazane_karte = tablica.okrenuta[stupac]
			if len(skrivene_karte) > x:
				print_str += "\tx"
			elif len(prikazane_karte) + len(skrivene_karte) > x:
				print_str += "\t" + str(prikazane_karte[x-len(skrivene_karte)])
			else:
				print_str += "\t"
		print(print_str)
	print("\n"+BREAK_STRING)

if __name__ == "__main__":
	s = Spil()
	t = Tablica([s.podijeli_karte(x) for x in range(1,8)])
	k = Kuca()
	p = Pricuva(s.podijeli_karte(24))
	prikaz=Prikaz()

	print("\n" + BREAK_STRING)
	print("Dobrodošli u našu igru! Sretno.")
	Naredbe()
	ispisiTablicu(t, k, p)


	while not k.pobjeda():
		naredba = input("Upisi naredbu ('p' za pomoć): ")
		naredba = naredba.lower().replace(" ", "")
		if naredba == "p":
			Naredbe()
		elif naredba == "q":
			print("Uzbudljiva igra!")
			break
		elif naredba == "mv":
			if p.izOtp_uPric():
				ispisiTablicu(t, k, p)
		elif naredba == "ok":
			if p.getOtp()=="prazno":
				print("Greska!")
			elif k.dodajKartu(p.getOtp()):
				p.pop_otp_karta()
				ispisiTablicu(t, k, p)
			else:
				print("Greska!")
		elif "ot" in naredba and len(naredba) == 3:
			stupac = int(naredba[-1]) - 1
			if t.izOtp_uTab(p, stupac):
				ispisiTablicu(t, k, p)
			else:
				print("Greska!")
		elif "tk" in naredba and len(naredba) == 3:
			stupac = int(naredba[-1]) - 1
			if t.izTab_uKucu(k, stupac):
				ispisiTablicu(t, k, p)
			else:
				print("Greska!")
		elif "tt" in naredba and len(naredba) == 4:
			c1, c2 = int(naredba[-2]) - 1, int(naredba[-1]) - 1
			if t.izTab_uTab(c1, c2):
				ispisiTablicu(t, k, p)
			else:
				print("Greska!")
		else:
			print("Naredba nije podržana.")

	if k.pobjeda():
		print("Cestitke!!! Pobijedili ste!")
