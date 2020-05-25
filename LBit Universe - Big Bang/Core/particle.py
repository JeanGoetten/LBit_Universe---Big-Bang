class Quark:
    def __init__(self, electric_charge, mass, color, spin):
        self.electric_charge = electric_charge
        self.mass            = mass
        self.color           = color
        self.spin            = spin

    def sniff(self):
        log = {
            'electric charge':  self.electric_charge,
            'mass':             str(self.mass) + " GeV",
            'color':            self.color,
            'spin':             self.spin
        }
        return log           

class Lepton:
    def __init__(self, electric_charge, mass, spin):
        self.electric_charge = electric_charge
        self.mass            = mass
        self.spin            = spin
    
    def sniff(self):
        log = {
            'electric charge':  self.electric_charge,
            'mass':             str(self.mass) + " GeV",
            'spin':             self.spin
        }
        return log

u = Quark(1, 190, 'red', 0.5)
d = Quark(1, 500, 'blue', -0.5)

eletron = Lepton(5, 800, 1)

print(u.mass)
print(d.sniff())
print(eletron.sniff())