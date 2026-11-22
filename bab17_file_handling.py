print('Dila - NIS 102576967')
with open("catatan.txt", "w") as f:
    f.write("Baris 1\nBaris 2\n")
with open("catatan.txt") as f:
    print(f.read())
