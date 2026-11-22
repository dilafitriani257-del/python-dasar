print('Dila - NIS 123456789')
class Kucing:
    def suara(self):
        return "Meong"

class Anjing:
    def suara(self):
        return "Guk guk"

for h in [Kucing(), Anjing()]:
    print(h.__class__.__name__, "->", h.suara())
