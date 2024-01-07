import random

accounts = {
    "Admin": ["12345", "rayshoesmith70@mail.com"],
    "User1": ["password", "user1@mail.com"],
    "User2": ["manypass", "user2@mail.com"],
    "User3": ["cantfindany", "user3@mail.com"],
}


def signup():
    print("<-------------------------------------------Kayıt Programı ---------------------------------------------------------->")
    
    while True:
        mail = input("Mail Adresinizi Giriniz: ")
        while "@" not in mail:
            print("Geçerli Bir Mail Adresi Girmeniz Gerekmektedir!")
            mail = input("Mail Adresinizi Giriniz: ")

        new_user = input("Kullanıcı Adı: ")
        for i in accounts:
            while new_user == i:
                print("Girilen Kullanıcı Adı Halihazırda Kullanımdadır, Lütfen Farklı Bir Kullanıcı Adı Seçiniz!")
                new_user = input("Kullanıcı Adı: ")

        trys = 0
        new_pass = input("Şifre: ")
        v_new_pass = input("Şifrenizi Doğrulayın: ")
        while new_pass != v_new_pass:
            print("Şifreler Eşleşmiyor, Lütfen Doğru Girdiğinize Emin Olunuz!")
            new_pass = input("Şifre: ")
            v_new_pass = input("Şifrenizi Doğrulayın: ")
            trys += 1
            if trys == 3:
                print("Çok Sayıda Geçersiz İşlem Yapıldı Program Kapatılıyor...")
                exit()

        accounts.update({new_user: [new_pass, mail]})
        print(f"Sayın Kullanıcı {new_user}, Kaydınız Başarıyla Gerçekleşmiştir!\nPrograma Yönlendiriliyorsunuz...")
        return True


def login():
    trys = 0
    wrong_pass = 0
    
    while True:
        username = input("Kullanıcı Adı : ")
        password = input("Şifre : ")

        for k, v in accounts.items():
            if username == k and password == v[0]:
                print("Giriş Başarılı!")
                return True
            elif username == k and password != v[0]:
                print("Hatalı Kullanıcı Adı Veya Şifre!")
                wrong_pass += 1
                if wrong_pass == 3:
                    ask_change = input("Şifrenizi Mi Unuttunuz? (E/H): ").upper()
                    if ask_change == "E":
                        return "Incorrect"
            elif username not in accounts:
                print("Böyle Bir Kullanıcı Bulunmamaktadır!")
                ask_signup = input("Kayıt Olmak İçin 'E' Tekrar Denemek İçin 'H' Tuşlayınız: ").upper()
                if ask_signup == "E":
                    return "Signup"
                elif ask_signup == "H":
                    return "Trying"
                else:
                    return False
            else:
                continue
        trys += 1
        if trys == 5:
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()


def changepass():
    print("<------Şifremi Unuttum------>")

    username = input("Kullanıcı Adınız: ") # Change that to mail 
    if username in accounts:
        vcode = random.randint(100000, 999999)
        print(vcode)
        verify = int(input(f"{accounts[username][1]} Mail Adresine Gelen 6 Haneli Doğrulama Kodunu Giriniz: "))
        
        if verify == vcode:
            changed_pass = input("Yeni Şifre: ")
            v_changed_pass = input("Yeni Şifryi Doğrulayın: ")
            while changed_pass != v_changed_pass:
                changed_pass = input("Yeni Şifre: ")
                v_changed_pass = input("Yeni Şifreyi Doğrulayın: ")
            accounts.update({username: [changed_pass, accounts[username][1]]})

    elif username not in accounts:
        print("Böyle Bir Kullanıcı Adı Bulunmamaktadır!")


while True:
    login_result = login()
    if login_result == True:
        exit()
    elif login_result == False:
        print("Invalid Argument! Shutting Down...")
        exit()
    elif login_result == "Incorrect":
        changepass()
    elif login_result == "Signup":
        signup()

# add-list
# import data from txt file
# make mail:[username,password]
