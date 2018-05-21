import pandas as pd
import numpy as np

class TinggiBadan():
    name = ""
    value = 0.0
    min = 0.0
    max = 0.0

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

class BeratBadan():
    name = ""
    value = 0.0
    min = 0.0
    max = 0.0

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

class Deffuzi():
    name = ""
    value = 0.0

    def __init__(self, name, value):
        self.name = name
        self.value = value

if __name__ == '__main__':
    def Hasil(obj1, obj2):
        if ((obj1.name == "Sangat Pendek") & (obj2.name == "Sangat Kurus")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Pendek") & (obj2.name == "Kurus")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Pendek") & (obj2.name == "Biasa")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Pendek") & (obj2.name == "Berat")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Pendek") & (obj2.name == "Sangat Berat")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        # --------------------------------------------------------------------------------------------------------------

        if ((obj1.name == "Pendek") & (obj2.name == "Sangat Kurus")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Pendek") & (obj2.name == "Kurus")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Pendek") & (obj2.name == "Biasa")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Pendek") & (obj2.name == "Berat")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Pendek") & (obj2.name == "Sangat Berat")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        # --------------------------------------------------------------------------------------------------------------

        if ((obj1.name == "Sedang") & (obj2.name == "Sangat Kurus")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sedang") & (obj2.name == "Kurus")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sedang") & (obj2.name == "Biasa")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sedang") & (obj2.name == "Berat")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sedang") & (obj2.name == "Sangat Berat")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        # --------------------------------------------------------------------------------------------------------------

        if ((obj1.name == "Tinggi") & (obj2.name == "Sangat Kurus")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Tinggi") & (obj2.name == "Kurus")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Tinggi") & (obj2.name == "Biasa")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Tinggi") & (obj2.name == "Berat")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Tinggi") & (obj2.name == "Sangat Berat")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        # --------------------------------------------------------------------------------------------------------------

        if ((obj1.name == "Sangat Tinggi") & (obj2.name == "Sangat Kurus")):
            return Deffuzi("Tidak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Tinggi") & (obj2.name == "Kurus")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Tinggi") & (obj2.name == "Biasa")):
            return Deffuzi("Sangat Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Tinggi") & (obj2.name == "Berat")):
            return Deffuzi("Sehat", min([obj1.value, obj2.value]))

        if ((obj1.name == "Sangat Tinggi") & (obj2.name == "Sangat Berat")):
            return Deffuzi("Agak Sehat", min([obj1.value, obj2.value]))

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

    # Tinggi Badan
    tBadan = []
    i = 0
    lebih = False
    for list in listTinggiBadan:
        if (inputTinggi > list.min) & (inputTinggi < list.max):
            if lebih == True:
                y = i
            else:
                lebih = True
                x = i
            list.value = 1
            tBadan.append(list)
        else:
            list.value = 0
        i += 1

    if (len(tBadan) == 2):
        tBadan[0].value = (tBadan[0].max - inputTinggi) / (tBadan[0].max - tBadan[1].min)
        tBadan[1].value = (inputTinggi - tBadan[1].min) / (tBadan[0].max - tBadan[1].min)
        if (tBadan[0].value > tBadan[1].value):
            ftBadan = Deffuzi(tBadan[0].name, tBadan[0].value)
        else:
            ftBadan = Deffuzi(tBadan[1].name, tBadan[1].value)
        listTinggiBadan[x].value = tBadan[0].value
        listTinggiBadan[y].value = tBadan[1].value

    else:
        tBadan[0].value = 1
        ftBadan = Deffuzi(tBadan[0].name, tBadan[0].value)
        listTinggiBadan[x].value = tBadan[0]

    # Berat Badan
    bBadan = []
    i = 0
    lebih = False
    for list in listBeratBadan:
        if (inputBerat > list.min) & (inputBerat < list.max):
            if lebih == True:
                y = i
            else:
                lebih = True
                x = i
            list.value = 1
            bBadan.append(list)
        else:
            list.value = 0
        i += 1

    if (len(tBadan) == 2):
        bBadan[0].value = (bBadan[0].max - inputBerat) / (bBadan[0].max - bBadan[1].min)
        bBadan[1].value = (inputBerat - bBadan[1].min) / (bBadan[0].max - bBadan[1].min)
        if (bBadan[0].value > bBadan[1].value):
            fbBadan = Deffuzi(bBadan[0].name, bBadan[0].value)
        else:
            fbBadan = Deffuzi(bBadan[1].name, bBadan[1].value)
        listBeratBadan[x].value = bBadan[0].value
        listBeratBadan[y].value = bBadan[1].value
    else:
        bBadan[0].value = 1
        fbBadan = Deffuzi(bBadan[0].name, bBadan[0].value)
        listBeratBadan[x].value = bBadan[0]

    print("")

    df = pd.DataFrame(index=['Sangat Pendek', 'Pendek', 'Sedang', 'Tinggi', 'Sangat Tinggi'], dtype=np.int)
    tampil = ['Sangat Kurus', 'Kurus', 'Biasa', 'Berat', 'Sangat Berat']
    for lisB in listBeratBadan:
        list = []
        i = 0
        for listT in listTinggiBadan:
            if listT.value == 0.0 or lisB.value == 0.0:
                list.append(0)
            else:
                list.append(min(listT.value, lisB.value))
        df[lisB.name] = pd.Series(list, index=['Sangat Pendek', 'Pendek', 'Sedang', 'Tinggi', 'Sangat Tinggi'])

    print(df)

    print("")

    print(ftBadan.name + "\t\t\t: " + str(ftBadan.value))
    print(fbBadan.name + "\t: " + str(fbBadan.value))

    hasil = Hasil(ftBadan, fbBadan)

    print("")

    print("Dari data di atas, hasilnya adalah : ")
    print(hasil.name + " dengan index " + str(hasil.value))