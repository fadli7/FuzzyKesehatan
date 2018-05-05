class TinggiBadan():
    name = ""
    value = 0
    min = 0
    max = 0

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

class BeratBadan():
    name = ""
    value = 0
    min = 0
    max = 0

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max


if __name__ == '__main__':
    sangatPendek = TinggiBadan("Sangat Pendek", 0, 120)
    pendek = TinggiBadan("Pendek", 115, 145)
    sedang = TinggiBadan("Sedang", 140, 165)
    tinggi = TinggiBadan("Tinggi", 160, 185)
    sangatTinggi = TinggiBadan("Sangat Tinggi", 180, 500)
    listTinggiBadan = [sangatPendek, pendek, sedang, tinggi, sangatTinggi]

    sangatKurus = BeratBadan("Sangat Kurus", 0, 45)
    kurus = BeratBadan("Kurus", 40, 55)
    biasa = BeratBadan("Biasa", 50, 65)
    berat = BeratBadan("Berat", 60, 85)
    sangatBerat = BeratBadan("Sangat Berat", 80, 200)
    listBeratBadan = [sangatKurus, kurus, biasa, berat, sangatBerat]

    inputTinggi = int(input("Masukkan Tinggi Anda\t: "))
    inputBerat = int(input("Masukkan Berat Badan\t: "))

    i = 0
    for list in listTinggiBadan:
        if (inputTinggi > list.min) & (inputTinggi < list.max):
            list.value = 1

            # print(list.name)
            # a = b = 1
            # nama = list.name
            # if i == 0:
            #     pembandingA = list
            #     namaA = list.name
            # else:
            #     pembandingB = list
            #     namaB = list.name
            # i += 1

    # if i == 2:
        # a = (pembandingA.max - inputTinggi) / (pembandingA.max - pembandingB.min)
        # b = (inputTinggi - pembandingB.min) / (pembandingA.max - pembandingB.min)
        # print(str(a) + " " + str(b))
    # if a == b:
    #     print(nama)
    #     print("Nilai : " + str(a))
    # else:
    #     print(namaA)
    #     print("Nilai : " + str(a))
    #
    #     print(namaB)
    #     print("Nilai : " + str(b))

    print('Tinggi Badan\t', end=":")
    for tampil in listTinggiBadan:
        print(str(tampil.value), end=', ')

    print("")

    i = 0
    for list in listBeratBadan:
        if (inputTinggi > list.min) & (inputTinggi < list.max):
            # print(list.name)
            a = b = 1
            nama = list.name
            if i == 0:
                pembandingA = list
                namaA = list.name
            else:
                pembandingB = list
                namaB = list.name
            i += 1
    if i == 2:
        a = (pembandingA.max - inputTinggi) / (pembandingA.max - pembandingB.min)
        b = (inputTinggi - pembandingB.min) / (pembandingA.max - pembandingB.min)
        # print(str(a) + " " + str(b))
    if a == b:
        print(nama)
        print("Nilai : " + str(a))
    else:
        print(namaA)
        print("Nilai : " + str(a))

        print(namaB)
        print("Nilai : " + str(b))