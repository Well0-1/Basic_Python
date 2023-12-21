students = {"2006": {
                'Adi': "Salih",
                'Soyadi': "Akyüzoğlu",
                'Tel No': "555-5555" },
            "478": {
                'Adi': "Muhammet",
                'Soyadi': "Akyüzoğlu",
                'Tel No': "521-1942" },
            "1223": {
                'Adi': "Yavuz Selim",
                'Soyadi': "Akyüzoğlu",
                'Tel No': "541-0581" },      
            "2006": {
                'Adi': "Muhammet Emin",
                'Soyadi': "Genç",
                'Tel No': "559-4808" }    
            }

while True:
    check = input("Kontrol Edilecek Öğrenci No: ")
    if check in students :
        print(f"{check} Numaralı Öğrenci Bilgileri :")
        for k, v in students[check].items() :
            print(f"{k}: {v}")
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