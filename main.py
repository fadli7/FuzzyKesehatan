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
    sangatPendek = TinggiBadan("Sangat Pendek", 0.0, 120.0)
    pendek = TinggiBadan("Pendek", 115.0, 145.0)
    sedang = TinggiBadan("Sedang", 140.0, 165.0)
    tinggi = TinggiBadan("Tinggi", 160.0, 185.0)
    sangatTinggi = TinggiBadan("Sangat Tinggi", 180.0, 500.0)
    listTinggiBadan = [sangatPendek, pendek, sedang, tinggi, sangatTinggi]

    sangatKurus = BeratBadan("Sangat Kurus", 0.0, 45.0)
    kurus = BeratBadan("Kurus", 40.0, 55.0)
    biasa = BeratBadan("Biasa", 50.0, 65.0)
    berat = BeratBadan("Berat", 60.0, 85.0)
    sangatBerat = BeratBadan("Sangat Berat", 80.0, 200.0)
    listBeratBadan = [sangatKurus, kurus, biasa, berat, sangatBerat]

    inputTinggi = float(input("Masukkan Tinggi Anda\t: "))
    inputBerat = float(input("Masukkan Berat Badan\t: "))

    i = 0
    for list in listTinggiBadan:
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

    print("")

    i = 0
    for list in listBeratBadan:
        if (inputBerat > list.min) & (inputBerat < list.max):
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
        a = (pembandingA.max - inputBerat) / (pembandingA.max - pembandingB.min)
        b = (inputBerat - pembandingB.min) / (pembandingA.max - pembandingB.min)
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
