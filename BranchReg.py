# """
# 1st way
branch = ["Yüzme", "Hentbol", "Basketbol", "Futbol", "Jimnastik"]
male = {"enes", "ufuk", "ulaş", "burak", "caner"}
female = {"nihal", "ipek", "özden"}

name = input("İsminizi Giriniz: ").lower()
if name in male:
    gender = "E"
elif name in female:
    gender = "K"
else:
    gender = ""

age = input("Yaşinizi Giriniz: ")
while not age.isdigit():
    print("Bir Tam Sayı Girmeniz Gerekmektedir.")
    age = input("Yaşinizi Giriniz: ")
age = int(age)

License = input("Futbol Lisansi Var mi ? (E/H)").upper()
print(f"{name}, {age} ({gender}) Katilabileceğiniz Kurslar:")
if age <= 6:
    print("Yüzme")
if age <= 8:
    print("Hentbol")
if age >= 20 and age <= 30:
    print("Basketbol")
if age >= 20 and age <= 35 and License == "E":
    print("Futbol")
else:
    print("Size Uygun Kursumuz Bulunmamaktadır.")
# """
#"""
# 2nd way
branch = ["Yüzme", "Hentbol", "Basketbol", "Futbol", "Jimnastik"]
male = {"enes", "ufuk", "ulaş", "burak", "caner"}
female = {"nihal", "ipek", "özden"}

name = input("İsminizi Giriniz: ")
if name in male:
    gender = "E"
elif name in female:
    gender = "K"
else:
    gender = ""

age = input("Yaşinizi Giriniz: ")
while not age.isdigit():
    print("Geçerli Bir Değer Girmeniz Gerekmektedir.")
    age = input("Yaşinizi Giriniz: ")
age = int(age)

print("Aktif Olan Branşlar:")

for sayi, k in enumerate(branch, start=1):
    print(f"{sayi}-){k}")
loop = "E"
while loop == "E" :
    req = input("Kaydolmak İstediğiniz Branşi Yaziniz: ").lower()
    if req == "yüzme" or req == "1":
        if age <= 6:
            print("Kayit olabilirsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
        else:
            print("Maalesef Kayit Olamazsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()

    if req == "hentbol" or req == "2":
        if 8 >= age:
            print("Kayit olabilirsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
        else:
            print("Maalesef Kayit Olamazsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
    if req == "basketbol" or req == "3":
        if 20 < age and 30 > age:
            print("Kayit olabilirsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
        else:
            print("Maalesef Kayit Olamazsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()

    if req == "futbol" or req == "4":
        License = input("Futbol Lisansi Var mi ? (E/H)").upper()
        if 20 < age and 35 > age and License == "E":
            print("Kayit olabilirsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
        else:
            print("Maalesef Kayit Olamazsiniz")
            loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()

    if req == "jimnastik" or req == "5":
        print("Maalesef Jimnastik Kursu Alimi Kapanmiştir")
        loop = input("Kayit olmak istediğiniz başka bir kurs var mı? (E/H): ").upper()
    if loop != "E" or loop != "H":
        print("Unvalid Argument Process Will be Terminated.")
#"""
