accounts = {"Admin":"12345",
            "User1":"password",
            "User2":"manypass",
            "User3":"cantfindany",
            }

def login() :
    trys = 10
    while True : 
        username = input("Kullanıcı Adı : ")
        password = input("Şifre : ")
        for k, v in accounts.items() :
            if username == k and password == v :
                print("Giriş Başarılı!")
                return False
            else :
                continue
        print("Geçersiz Kullanıcı Adı Veya Şifre Lütfen Tekrar Deneyiniz!")
        trys -= 1
        if trys == 0 :
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()
login()

# add-list
# signup **kwargs 
# import data from txt file 
# change password 