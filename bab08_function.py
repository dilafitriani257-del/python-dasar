print('Dila - NIS 123456789')
NIS=123456789
mkdir -p ~/dila/python-dasar && cd ~/dila/python-dasar
git init -q -b main
git config --local user.name "Dila"
git config --local user.email "dilafitriani257@gmail.com"
git config --local core.sshCommand "ssh -i ~/.ssh/id_ed25519_dila -o IdentitiesOnly=yes"
git config --local core.pager cat
python3 -m venv venv && mkdir -p screenshots
printf "venv/\n__pycache__/\n.env\n" > .gitignore
source venv/bin/activate

mk() { { echo "print('Dila - NIS $NIS')"; cat; } > "$1"; }
c() { git add . && git commit -q -m "feat(dasar): $1" -m "- Tambahkan $2" && echo "OK: $1"; }

mk bab01_pengenalan.py <<'EOF'
import sys
print("Hello, Python!")
print("Versi Python:", sys.version.split()[0])
EOF
c "pengenalan dan instalasi python" bab01_pengenalan.py

mk bab02_struktur.py <<'EOF'
def main():
    nama = "Dila"
    if nama:
        print("Halo,", nama)

if __name__ == "__main__":
    main()
EOF
c "struktur dasar program python" bab02_struktur.py

mk bab03_tipe_data.py <<'EOF'
print(10, type(10))
print(3.14, type(3.14))
print("teks", type("teks"))
print(True, type(True))
print(None, type(None))
EOF
c "tipe data dasar" bab03_tipe_data.py

mk bab04_variable.py <<'EOF'
nama = "Dila"
jumlah = 5
a, b = 1, 2
print(nama, jumlah, a, b)
jumlah = jumlah + 1
print("Jumlah baru:", jumlah)
EOF
c "variable" bab04_variable.py

mk bab05_konstanta.py <<'EOF'
PI = 3.14159
JUMLAH_HARI = 7
r = 5
print("Luas lingkaran:", PI * r ** 2)
print("Hari dalam seminggu:", JUMLAH_HARI)
EOF
c "konstanta" bab05_konstanta.py

mk bab06_operator.py <<'EOF'
a, b = 10, 3
print(a + b, a - b, a * b, a / b)
print(a // b, a % b, a ** b)
print(a > b, a == b)
print(a > 5 and b < 5, a > 5 or b > 5, not a > 5)
EOF
c "operator" bab06_operator.py

mk bab07_control_flow.py <<'EOF'
nilai = 80
if nilai >= 85:
    print("Grade A")
elif nilai >= 70:
    print("Grade B")
else:
    print("Grade C")
for i in range(1, 4):
    print("for ke-", i)
n = 3
while n > 0:
    print("while:", n)
    n -= 1
EOF
c "control flow" bab07_control_flow.py

mk bab08_function.py <<'EOF'
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

def luas(p, l):
    return p * l

print(sapa("Dila"))
print(sapa("Ani", "Selamat pagi"))
print("Luas:", luas(5, 3))
EOF
c "function" bab08_function.py

mk bab09_list_tuple_set.py <<'EOF'
buah = ["apel", "jeruk"]
buah.append("mangga")
koordinat = (10, 20)
angka = {1, 2, 2, 3}
print("List:", buah)
print("Tuple:", koordinat)
print("Set:", angka)
EOF
c "list, tuple, dan set" bab09_list_tuple_set.py

mk bab10_dictionary.py <<'EOF'
siswa = {"nama": "Dila", "kelas": "XI"}
siswa["hobi"] = "coding"
for k, v in siswa.items():
    print(k, ":", v)
print("Kunci:", list(siswa.keys()))
EOF
c "dictionary" bab10_dictionary.py

mk bab11_class_object.py <<'EOF'
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Saya {self.nama}, kelas {self.kelas}"

print(Siswa("Dila", "XI").perkenalan())
print(Siswa("Ani", "XII").perkenalan())
EOF
c "class dan object (oop dasar)" bab11_class_object.py

mk bab12_encapsulation.py <<'EOF'
class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

r = Rekening(1000)
r.setor(500)
print("Saldo:", r.saldo)
EOF
c "encapsulation" bab12_encapsulation.py

mk bab13_inheritance.py <<'EOF'
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
EOF
c "inheritance" bab13_inheritance.py

mk bab14_polymorphism.py <<'EOF'
class Kucing:
    def suara(self):
        return "Meong"

class Anjing:
    def suara(self):
        return "Guk guk"

for h in [Kucing(), Anjing()]:
    print(h.__class__.__name__, "->", h.suara())
EOF
c "polymorphism" bab14_polymorphism.py

mk bab15_abstraction.py <<'EOF'
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, s):
        self.s = s

    def luas(self):
        return self.s ** 2

print("Luas persegi:", Persegi(4).luas())
EOF
c "abstraction" bab15_abstraction.py

mk bab16_exception.py <<'EOF'
try:
    angka = int("abc")
except ValueError:
    print("Input bukan angka")
finally:
    print("Selesai")

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error:", e)
EOF
c "exception handling" bab16_exception.py

mk bab17_file_handling.py <<'EOF'
with open("catatan.txt", "w") as f:
    f.write("Baris 1\nBaris 2\n")
with open("catatan.txt") as f:
    print(f.read())
EOF
c "file handling (read dan write file)" bab17_file_handling.py

cat > modul_matematika.py <<'EOF'
def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b
EOF
mk bab18_module.py <<'EOF'
import modul_matematika
from modul_matematika import kali
print("Tambah:", modul_matematika.tambah(2, 3))
print("Kali:", kali(4, 5))
EOF
c "module" "bab18_module.py dan modul_matematika.py"

mkdir -p paket_hewan && touch paket_hewan/__init__.py
cat > paket_hewan/hewan.py <<'EOF'
def suara():
    return "Meong"
EOF
mk bab19_package.py <<'EOF'
from paket_hewan.hewan import suara
print("Suara:", suara())
EOF
c "package" "bab19_package.py dan folder paket_hewan"

git remote add origin git@github.com:dilafitriani257-del/python-dasar.git 2>/dev/null || git remote set-url origin git@github.com:dilafitriani257-del/python-dasar.git
git push -u origin main
