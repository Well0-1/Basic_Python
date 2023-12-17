students = {}

print("Öğrenci Kayit Sistemi Yükleniyor...")
def reg(loop="E"):
    while loop == "E" :
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
        if loop == "E":
            continue
        elif loop == "H":
            print("Kaydedilen Öğrenci Bilgileri:")    
            for f,l in students.items():
                print(f"{f} Numarali Öğrenci: {l}")
        elif loop != "E" or loop != "H":
            print("Unvalid Argument Process Will Be Terminated:")    
            for f,l in students.items():
                print(f"{f} Numarali Öğrenci: {l}")
                break
reg()