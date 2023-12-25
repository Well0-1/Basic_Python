students = {}

# Before I added the other functions
def check_in_terminal():
    while True:
        check = input("Kontrol Edilecek Öğrenci No: ")
        if check in students :
            print(f"{check} Numaralı Öğrenci Bilgileri :")
            for key, value in students[check].items() :
                print(f"{key}: {value}")
            loop = input("Farklı Bir Öğrenci Kontrol Etmek İstiyor musunuz? (E/H) ").upper()
            if loop == "E":
                continue
            else :
                print("Program Kapanıyor...")
                break
        elif not check in students :
            print("Böyle Bir Öğrenci Bulunmamaktadır")
            loop = input("Farklı Bir Öğrenci Kontrol Etmek İstiyor musunuz? (E/H) ").upper()
            if loop == "E":
                continue
            else : 
                print("Program Kapanıyor...")
                break
#

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
            
def check_info() :
    while True:
        check = input("Kontrol Edilecek Öğrenci No: ")    
        
        if check in students:
            print(f"{check} Numaralı Öğrenci Bilgileri :")
            for key, value in students[check].items():
                print(f"{key}: {value}")
            break
        else:  
            print("Böyle Bir Öğrenci Bulunmamaktadır")
            continue

read_from_file()

check_info()
