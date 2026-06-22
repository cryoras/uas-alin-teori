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

def gauss_ordo_4(matriks):

    # Salin matriks agar matriks asli tidak berubah
    A = [baris[:] for baris in matriks]
    ukuran = len(A)

    for kolom in range(ukuran):

        # Cari baris dengan pivot terbesar
        pivot_row = kolom

        for baris in range(kolom + 1, ukuran):
            if abs(A[baris][kolom]) > abs(A[pivot_row][kolom]):
                pivot_row = baris

        # Tukar baris bila diperlukan
        if pivot_row != kolom:
            A[kolom], A[pivot_row] = A[pivot_row], A[kolom]

        # Cek matriks singular
        if abs(A[kolom][kolom]) < 1e-12:
            raise ValueError(
                "Sistem tidak memiliki solusi unik."
            )

        # Eliminasi elemen di bawah pivot
        for baris in range(kolom + 1, ukuran):

            faktor = A[baris][kolom] / A[kolom][kolom]

            for j in range(kolom, ukuran + 1):
                A[baris][j] -= faktor * A[kolom][j]

    #back subtituion
    solusi = [0] * ukuran 
    for i in range(ukuran - 1, -1, -1):

        total_terhitung = 0


        for j in range(i + 1, ukuran):

            koefisien = A[i][j]
            nilai_variabel = solusi[j]

            total_terhitung += koefisien * nilai_variabel

        ruas_kanan = A[i][ukuran]
        koefisien_diagonal = A[i][i]

        solusi[i] = (
            ruas_kanan - total_terhitung
        ) / koefisien_diagonal

    print("W = ",solusi[0])
    print("X = ",solusi[1])
    print("Y = ",solusi[2])
    print("Z = ",solusi[3])


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
