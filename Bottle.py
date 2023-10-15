class Bottle:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self.objemLitry = 0
        self.zavrena = True

    def ziskej_litry(self):
        return self.objemLitry

    def nastav_litry(self, objem):
        if not self.zavrena:
            if objem <= self.kapacita:
                self.objemLitry = objem
            else:
                self.objemLitry = self.kapacita
        else:
            print("Lahev je zavrena.")

    def vyprazdni(self):
        if not self.zavrena:
            self.objemLitry = 0
        else:
            print("Lahev je zavrena.")

    def ziskej_objem_v_mililitrech(self):
        return self.objemLitry * 1000

    def nastav_mililitry(self, objem_ml):
        self.nastav_litry(objem_ml / 1000)

    def otevri(self):
        self.zavrena = False

    def zavri(self):
        self.zavrena = True

bootle = Bottle(2.0) 

bootle.otevri() 
bootle.nastav_litry(1.5)  
print("Objem v litrech:", bootle.ziskej_litry())
bootle.nastav_mililitry(500)  
print("Objem v litrech:", bootle.ziskej_litry())
print("Objem v mililitrech:", bootle.ziskej_objem_v_mililitrech())
bootle.vyprazdni()  
print("Objem v litrech po vyprázdnění:", bootle.ziskej_litry())
bootle.zavri()  

