accounts = {"Admin":"12345",
            "User1":"password",
            "User2":"manypass",
            "User3":"cantfindany",
            }

    
def signup() :
    print("-------------------------------------------Kayıt Programı ----------------------------------------------------------")
    while True :
        new_user = input("Kullanıcı Adı: ")
        for i in accounts :
            while new_user == i :
                    print("Girilen Kullanıcı Adı Halihazırda Kullanımdadır, Lütfen Farklı Bir Kullanıcı Adı Seçiniz!")
                    new_user = input("Kullanıcı Adı: ")
        new_pass = input("Şifre: ") 
        
        accounts.update({new_user:new_pass})
        print(f"Sayın Kullanıcı {new_user}, Kaydınız Başarıyla Gerçekleşmiştir!\nPrograma Yönlendiriliyorsunuz...")    
        return True

def login() :
    trys = 0
    wrong_pass = 0
    while True : 
        
        username = input("Kullanıcı Adı : ")
        password = input("Şifre : ")
        
        for k, v in accounts.items() :
            if username == k and password == v :
                print("Giriş Başarılı!")
                return True
            elif username == k and password != v :
                print("Hatalı Kullanıcı Adı Veya Şifre")
                wrong_pass += 1
                if wrong_pass == 3 :
                    ask_change = input("Şifrenizi Mi Unuttunuz? (E/H): ").upper()
                    if ask_change == "E":
                        return "Incorrect"
            elif username not in accounts :
                print("Böyle Bir Kullanıcı Bulunmamaktadır")
                ask_signup = input("Kayıt Olmak İçin 'E' Tekrar Denemek İçin 'H' Tuşlayınız: ").upper()
                if ask_signup == "E":
                    return "Signup"
                else :
                    return False
            else :
                continue   
        trys += 1
        if trys == 5 :
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()

def changepass() :
    print("Working on it")

while True :
    login_result = login()
    if login_result == True :
        exit()
    elif login_result == "Incorrect" :
        changepass()
    elif login_result == "Signup" :
        signup()



# add-list
# import data from txt file 
# change password 
