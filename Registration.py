students = {}

print("Öğrenci Kayit Sistemi Yükleniyor...")

def reg(loop="E") :
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
        else :
            print("Unvalid Argument Process Will Be Terminated:")    
            for f,l in students.items():
                print(f"{f} Numarali Öğrenci: {l}")
            break

# Saves student information to txt file
def save_students_info():
    with open("students_info.txt", "w") as file:
        for number, info in students.items():
            file.write(f"{number},{info['Adi']},{info['Soyadi']},{info['Tel No']}\n")

reg()
save_students_info()
