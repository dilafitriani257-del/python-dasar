print('Dila - NIS 123456789')
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Saya {self.nama}, kelas {self.kelas}"

print(Siswa("Dila", "XI").perkenalan())
print(Siswa("Ani", "XII").perkenalan())
