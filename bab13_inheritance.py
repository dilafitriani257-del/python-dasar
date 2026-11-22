print('Dila - NIS 123456789')
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        return f"Ini {self.nama}"

class Kucing(Hewan):
    def suara(self):
        return "Meong"

k = Kucing("Tom")
print(k.info(), "-", k.suara())
