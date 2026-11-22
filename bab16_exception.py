print('Dila - NIS 102576967')
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
