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

def gauss_ordo_1(m):
    a = m[0][0]
    b = m[0][1]
    if a == 0:
        print("Koefisien bernilai 0")
        return
    x = b / a
    print("\nHasil:")
    print("x =", x)

def gauss_ordo_2(m):
    
    if m[0][0] == 0:
        print("Pivot bernilai 0")
        return

    faktor = m [1][0] / m[0][0]

    for j in range(3):
        m[1][j] = m[1][j] - faktor * m[0][j]

    print("Matriks setelah eliminasi:")
    for baris in m:
        print(baris)

    if m[1][1] == 0:
        print("Sistem tidak memiliki solusi unik")
        return

    y = m[1][2] / m[1][1]

    x = (m[0][2] - m[0][1] * y) / m[0][0]

    print("\nHasil:")
    print("x =", x)
    print("y =", y)

def gauss_ordo_3(m):
    # Eliminasi maju
    for i in range(3):
        if m[i][i] == 0:
            print("Pivot bernilai 0, sistem tidak memiliki solusi unik.")
            return
        for j in range(i + 1, 3):
            faktor = m[j][i] / m[i][i]
            for k in range(4):
                m[j][k] = m[j][k] - faktor * m[i][k]

    print("\nMatriks setelah eliminasi:")
    for baris in m:
        print(baris)

    # Substitusi mundur
    z = m[2][3] / m[2][2]
    y = (m[1][3] - m[1][2] * z) / m[1][1]
    x = (m[0][3] - m[0][2] * z - m[0][1] * y) / m[0][0]

    print("\nHasil:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")

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
    print("=" * 40)
    print("   ELIMINASI GAUSS")
    print("=" * 40)
    print("Pilih ordo sistem persamaan:")
    print("  1. Ordo 1  (1 variabel)")
    print("  2. Ordo 2  (2 variabel)")
    print("  3. Ordo 3  (3 variabel)")
    print("  4. Ordo 4  (4 variabel)")

    pilihan = int(input("\nPilihan: "))

    if pilihan == 1:
        matriks = input_matriks(1, 2)
        gauss_ordo_1(matriks)
    elif pilihan == 2:
        matriks = input_matriks(2, 3)
        gauss_ordo_2(matriks)
    elif pilihan == 3:
        matriks = input_matriks(3, 4)
        gauss_ordo_3(matriks)
    elif pilihan == 4:
        matriks = input_matriks(4, 5)
        gauss_ordo_4(matriks)
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
