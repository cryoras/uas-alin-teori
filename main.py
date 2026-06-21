# Ordo 1 (1 variabel)
ordo_1 = [
    [3, 9]
]

# Ordo 2 (2 variabel)
ordo_2 = [
    [2, 1, 5],
    [4, 3, 11]
]

# Ordo 3 (3 variabel)
ordo_3 = [
    [ 2,  1, -1,   8],
    [-3, -1,  2, -11],
    [-2,  1,  2,  -3]
]

# Ordo 4 (4 variabel)
ordo_4 = [
    [1, 1, 1, 1, 10],
    [2, 3, 4, 5, 40],
    [3, 5, 8, 9, 69],
    [1, 2, 3, 5, 30]
]

def gauss_ordo_1():
  pass

def gauss_ordo_2():
  pass

def gauss_ordo_3(m):
    # Eliminasi maju
    for i in range(3):
        if m[i][i] == 0:
            print("Pivot bernilai 0")
            return

        for j in range(i + 1, 3):
            faktor = m[j][i] / m[i][i]

            for k in range(4):
                m[j][k] = m[j][k] - faktor * m[i][k]

    print("Matriks setelah eliminasi:")
    for baris in m:
        print(baris)

    # Substitusi mundur
    z = m[2][3] / m[2][2]

    y = (m[1][3] - m[1][2] * z) / m[1][1]

    x = (m[0][3] - m[0][2] * z - m[0][1] * y) / m[0][0]

    print("\nHasil:")
    print("x =", x)
    print("y =", y)
    print("z =", z)


# Input matriks augmented 3x4
matrix = []

print("Masukkan elemen matriks augmented 3x4:")

for i in range(3):
    baris = []
    for j in range(4):
        nilai = float(input(f"Baris {i+1} Kolom {j+1}: "))
        baris.append(nilai)
    matrix.append(baris)

gauss_ordo_3(matrix)

def gauss_ordo_4():
  pass


def main():
    print("1. Ordo 1")
    print("2. Ordo 2")
    print("3. Ordo 3")
    print("4. Ordo 4")

    pilihan = int(input())

    if pilihan == 1:
        gauss_ordo_1()
    elif pilihan == 2:
        gauss_ordo_2()
    elif pilihan == 3:
        gauss_ordo_3()
    elif pilihan == 4:
        gauss_ordo_4()
