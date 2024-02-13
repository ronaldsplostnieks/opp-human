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
        sveiki_galotne = "a"
        laimests_galotne = "usi"
        laimests = self.age*35

        teksts = "Sveik{}(-a/-s/-i), {}(Vārds)! Tu esi laimēj{}(-usi/-is) {}(vecums*35)€!".format(sveiki_galotne, self.name, laimests_galotne, laimests)

        with open(faila_nosaukums, "w", encoding="utf-8") as spams:
            spams.write(teksts)

        self.nopelnit(laimests)
        self.pastastit_par_sevi()
        



persona1 = Cilveks("Marta", 32, "nenosakams")
persona1.pastastit_par_sevi()
persona1.dzimsanas_diena()
persona1.pastastit_par_sevi()
# persona1.nopelnit(30)
persona1.pastastit_par_sevi()
persona1.uztaisit_spamu("oop/spams/")

# turpinat = "t"
# cilveki = []
# while turpinat == "t":
#     vards = input("Ievadiet cilvēka vārdu!: ")
#     vecums = int(input("Ievadiet vecumu!: "))
#     dzimums = input("Ievadiet dzimumu (s/v)!:")
#     cilveki.append( Cilveks(vards, vecums, dzimums) )
#     turpinat = input("Ja vēlies pievienot vēl vienu cilvēku, nospied 't' !")

# for viens in cilveki:
    


