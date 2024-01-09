students = {}

# Student İnformation And Registiration System

def read_from_file() :
    with open("students_info.txt","r") as file : 
        lines = file.readlines()
        for line in lines :
            data = line.strip().split(",")
            number = data[0]
            name = data[1]
            lname = data[2]
            phone = data[3]
            students[number] = {"Adi": name, "Soyadi": lname, "Tel No" : phone}  
    return students

def save_students_info():
    with open("students_info.txt", "w") as file:
        for number, info in students.items():
            file.write(f"{number},{info['Adi']},{info['Soyadi']},{info['Tel No']}\n")

def registiration() :
    print("Öğrenci Kayit Sistemi Yükleniyor...")
    while True :
        number = input("Öğrenci No: ")
        name = input("Öğrenci Adi: ")
        surname = input("Öğrenci Soyadi: ")
        phone = input("Öğrenci Telefon: ")
        
        students.update({
            number: {
                'Adi': name,
                'Soyadi': surname,
                'Tel No': phone 
            }
        })

        loop = input("Yeni Bir Öğrenci Kaydetmek İstiyor musunuz? (E/H)").upper()

        if loop == "H":
            print("Kaydedilen Öğrenci Bilgileri:")    
            for f,l in students.items():
                print(f"{f} Numarali Öğrenci: {l}")
                break
        elif loop == "E":
            continue
        else:
            print("Unvalid Argument! Shutting Down")

def check_info() :
    while True:
        check = input("Kontrol Edilecek Öğrenci No: ")
        
        if check in students:
            print(f"{check} Numaralı Öğrenci Bilgileri :")
            for key, value in students[check].items():
                print(f"{key}: {value}")
            loop = input("Farklı Bir Öğrenci Kontrol Etmek İstiyor musunuz? (E/H): ").upper()
            if loop == "H":
                break
            
        else :
            print("Böyle Bir Öğrenci Bulunmamaktadır.")
            loop = input("Farklı Bir Öğrenci Kontrol Etmek İçin 'E' Programı Kapatmak İçin 'H' Tuşlayınız. ").upper()
            if loop == "E" :
                continue
            else :
                break 

while True :
    action = input("1.Öğrenci Kayıt Sistemi (Student Registiration)\n2.Öğrenci Bilgi Sistemi (Student İnformation System)\nSeçiniz: ").capitalize()
    if action in ["1","Kayıt","Registiration","Student registiration"] :
        registiration()
        save_students_info()
    elif action in ["2","Bilgi", "Görüntüleme","İnfo"]:
        read_from_file()
        check_info()
    else :
        print("Unvalid Argument! Shutting Down")
        exit()
