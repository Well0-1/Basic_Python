import random
import qrcode # Works On Python 3.8.2

accounts = {
    "rayshoesmith70@mail.com": ["Admin", "12345"],
    "user1@mail.com": ["User1", "password"],
    "user2@mail.com": ["User2", "manypass"],
    "user3@mail.com": ["User3", "cantfindany"],
}


def signup():
    print("<-----------------------------------------Kayıt Programı----------------------------------------->")

    mail = input("Mail Adresinizi Giriniz: ")
    for i in accounts :
        while mail == i :
            pswchg = input("Girilen Mail Adresi Halihazırda Kayıtlıdır, Kayıt Olmaya Devam Etmek İçin 'E', Şifrenizi Unuttuysanız 'H', Programı Kapatmak İçin 'Q' Tuşlayınız: ").upper()
            if pswchg == "E" :
                mail = input("Mail Adresinizi Giriniz: ")
            elif pswchg == "H":
                return 'Change_Pass'
            else:
                return False
    while "@" not in mail:
        print("Geçerli Bir Mail Adresi Girmeniz Gerekmektedir!")
        mail = input("Mail Adresinizi Giriniz: ")

    new_user = input("Kullanıcı Adı: ")

    while any(new_user == v[0] for v in accounts.values()) :
        print("Girilen Kullanıcı Adı Halihazırda Kullanımdadır, Lütfen Farklı Bir Kullanıcı Adı Seçiniz!")
        new_user = input("Kullanıcı Adı: ")

    trys = 0
    
    new_pass = input("Şifre: ")
    while len(new_pass) < 8 or len(new_pass) > 16 :
        print("Oluşturacağınız Şifre En Az 8 En Fazla 16 Karakter Olmalıdır!")
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

    accounts.update({mail: [new_user, new_pass]})
    print(f"Sayın Kullanıcı {new_user}, Kaydınız Başarıyla Gerçekleşmiştir!\nPrograma Yönlendiriliyorsunuz...")
    return True


def login():
    trys = 0
    wrong_pass = 0
    
    while True:
        username = input("Kullanıcı Adı : ")
        password = input("Şifre : ")

        for v in accounts.values():
            if username == v[0] and password == v[1]:
                print("Giriş Başarılı!")
                return True
            elif username == v[0] and password != v[1]:
                print("Hatalı Kullanıcı Adı Veya Şifre!")
                wrong_pass += 1
                if wrong_pass == 3:
                    ask_change = input("Şifrenizi Mi Unuttunuz? (E/H): ").upper()
                    if ask_change == "E":
                        return "Incorrect"
            elif not any(username == v[0] for v in accounts.values()) :
                print("Böyle Bir Kullanıcı Bulunmamaktadır!")
                ask_signup = input("Kayıt Olmak İçin 'E' Tekrar Denemek İçin 'H' Tuşlayınız: ").upper()
                if ask_signup == "E":
                    return "Signup"
                elif ask_signup == "H":
                    return "Try Again"
                else:
                    return False
            else:
                continue
        trys += 1
        if trys == 5:
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()


def changepass():
    print("<-----------Şifremi Unuttum----------->")

    mail = input("Mail Adresiniz: ") 
    if mail in accounts:
        username = accounts[mail][0]
        vcode = random.randint(100000, 999999)
        img = qrcode.make(vcode)              # Qr
        img.show()                            # Qr
        
        trys = 0
        while trys < 3 :
            verify = int(input(f"{mail} Adresine Gelen 6 Haneli Doğrulama Kodunu Giriniz: "))
            if verify == vcode:
                changed_pass = input("Yeni Şifre: ")
                v_changed_pass = input("Yeni Şifreyi Doğrulayın: ")
                while changed_pass != v_changed_pass:
                    changed_pass = input("Yeni Şifre: ")
                    v_changed_pass = input("Yeni Şifreyi Doğrulayın: ")
                accounts.update({mail:[username, changed_pass]})
                print("Şifreniz Başarıyla Değiştirildi!\n")
                break
            else :
                print("\nGirilen Kod Yanlış!\n")
                trys += 1
        if trys == 3 :
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()

    elif mail not in accounts:
        print("Bu Mail Adresine Kayıtlı Bir Kullanıcı Bulunmamaktadır!")
        ask_signup = input("Kayıt Olmak İster misiniz? (E/H): ").upper()
        if ask_signup == "E":
            return "Signup"
        else:
            return "Incorrect"


while True:
    login_result = login()
    if login_result == True:
        exit()
        
    elif login_result == False:
        print("Invalid Argument! Shutting Down...")
        exit()
        
    elif login_result == "Incorrect":
        chgpass_result = changepass()
        if chgpass_result == "Signup":
            signup()
        else :
            continue
               
    elif login_result == "Signup":
        signup_result = signup()
        if signup_result == "Change_Pass":
            changepass()
        elif signup_result == False :
            exit()
    else :
        continue

# add-list
# import data from txt file
# print("********** Login System **********")
# print(1.Signup)
# print(2.Login)
# print(3.Exit)
