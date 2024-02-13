# KM - Pabeigt objekta satura ierakstīšanu dokumentā. Nodrošināt, 
# lai programma prasa ievades datus objektiem kamēr cilvēks vēlas. 
# Visi objekti saglabāti sarakstā. Kad visi izveidoti, 
# visiem saraksta elementiem tiek izsaukta metode, 
# kas izveido teksta failus katram objektam.
class Cilveks:
    def __init__(self, vards, vecums, dzimums):
        self.age = vecums
        self.name = vards
        self.sex = dzimums
        self.nauda = 0

    def dzimsanas_diena(self):
        self.age += 1
    
    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards
    
    def pastastit_par_sevi(self):
        if self.sex == "s":
            dz = "sieviete"
        elif self.sex == "v":
            dz = "vīrietis"
        else:
            dz = self.sex
        print("Mani sauc {}, man ir {} gadi, es esmu {}".format(self.name, self.age, dz))

    def uztaisit_spamu(self, spama_mape):
        faila_nosaukums = spama_mape + "spams" + self.name + str(self.age) + ".txt"
        if self.sex == "s":
            sveiki_galotne = "a"
            laimests_galotne = "usi"
        elif self.sex == "v":
            sveiki_galotne = 's'  
            laimests_galotne = "is"  
        else:
            sveiki_galotne = "i"
            laimests_galotne = "is" 

        
        laimests = self.age*35

        teksts = "Sveik{}, {}! Tu esi laimēj{} {}€!".format(sveiki_galotne, self.name, laimests_galotne, laimests)

        with open(faila_nosaukums, "w", encoding="utf-8") as spams:
            spams.write(teksts)

        # self.nopelnit(laimests)
        self.pastastit_par_sevi()
        



# persona1 = Cilveks("Marta", 32, "nenosakams")
# persona1.uztaisit_spamu("spam/")

turpinat = "t"
cilveki = []
while turpinat == "t":
    vards = input("Ievadiet cilvēka vārdu!: ")
    vecums = int(input("Ievadiet vecumu!: "))
    dzimums = input("Ievadiet dzimumu (s/v)!:")
    cilveki.append( Cilveks(vards, vecums, dzimums) )
    turpinat = input("Ja vēlies pievienot vēl vienu cilvēku, nospied 't' !")

for viens in cilveki:
    viens.uztaisit_spamu("spam/")
    


