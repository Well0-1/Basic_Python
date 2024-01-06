accounts = {"Admin":"12345",
            "User1":"password",
            "User2":"manypass",
            "User3":"cantfindany",
            }

    
def signup() :
    ask_signup = input("Kayıt Olmak İçin 'E', Tekrar Denemek İçin 'H', Programı Kapatmak İçin 'Q' Tuşlayınız (E/H/Q) : ").upper()
    
    if ask_signup == "E" :
        print("-------------------------------------------Kayıt Programı ----------------------------------------------------------")
        while True :
            new_user = input("Kullanıcı Adı: ")
            for i in accounts :
                while new_user == i :
                        print("Girilen Kullanıcı Adı Halihazırda Kullanımdadır Lütfen Farklı Bir Kullanıcı Adı Seçiniz!")
                        new_user = input("Kullanıcı Adı: ")

            new_pass = input("Şifre: ") 
            accounts.update({new_user:new_pass})
            print(f"Sayın Kullanıcı {new_user}, Kaydınız Başarıyla Gerçekleşmiştir!\nPrograma Yönlendiriliyorsunuz...")    
            return True
    elif ask_signup == "H" :
        return False
    else : 
        print("Program Kapatılıyor...")
        exit()    

    
def login() :
    trys = 0
    
    while True : 
        
        username = input("Kullanıcı Adı : ")
        password = input("Şifre : ")
    
        if not username in accounts :
            print("Böyle Bir Kullanıcı Bulunmamaktadır!")
            break
    
        for k, v in accounts.items() :
            if username == k and password == v :
                print("Giriş Başarılı!")
                return True
            else :
                continue
        print("Hatalı Kullanıcı Adı Veya Şifre")        
        
        trys += 1
        if trys == 5 :
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()

while True :
    if login() == True :
        exit()
    signup()



# add-list
# import data from txt file 
# change password 
