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
