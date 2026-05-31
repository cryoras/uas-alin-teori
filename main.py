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

def gauss_ordo_3():
  pass

def matriks_4(matriks):
    # copy martrix dan dapatkan panjang matrix nya
    A = [row[:] for row in matriks]
    n = len(A)
    
    # eliminasi maju untuk seitap baris
    for k in range(n):
        # cari nilai pivot nya
        max_row = k
        for r in range(k + 1, n):
            if abs(A[r][k]) > abs(A[max_row][k]):
                max_row = r
                
        # Jika baris dengan nilai terbesar bukan baris k, lakukan pertukaran
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
        
        # jika elemen diagonal nya tetep 0 maka tidak memilik solusi unik
        if abs(A[k][k]) < 1e-12: 
            raise ValueError("Sistem tidak memiliki solusi unik (Matriks Singular).")

        # Proses eliminasi baris di bawahnya
        for i in range(k + 1, n):
            faktor = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] -= faktor * A[k][j]
                
    # implementasi back subsitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
            
        x[i] = (A[i][n] - sum_ax) / A[i][i]
        
    return x


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
       ans = matriks_4(ordo_4)
       print(f"Solusi dari matrikx ordo 4 x1 = {ans[0}, x2 = {ans[1]}, x3 = {ans[2]}, x4 = {ans[3}")
