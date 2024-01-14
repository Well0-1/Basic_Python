import os 
import random
# import qrcode                              # Works On Python 3.8.2
from cryptography.fernet import Fernet as F  # Works On Python 3.8.2 
import maskpass                              # Works On Python 3.8.2



if not os.path.exists("Accounts.txt"):
    open("Accounts.txt","x")

def generate_key():
    key = F.generate_key()
    with open("key.key","wb") as key_file :
        key_file.write(key)     

if not os.path.exists("key.key"):
    generate_key()

def save_key():
    return open("key.key", "rb").read()            
    
key = save_key()

encryptor = F(key)

accounts = {} 


def accounts_read():
    with open("Accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split("|")
            mail = encryptor.decrypt(data[0][2:-1]).decode()
            username = encryptor.decrypt(data[1][2:-1]).decode()
            password = encryptor.decrypt(data[2][2:-1]).decode()
            accounts[mail] = [username, password]
    return accounts


def accounts_save():
    with open("Accounts.txt", "w") as file:
        for mail, info in accounts.items():
            encrypt_mail = encryptor.encrypt(mail.encode())
            encrypt_info0 = encryptor.encrypt(info[0].encode())
            encrypt_info1 = encryptor.encrypt(info[1].encode())
            file.write(f"{encrypt_mail}|{encrypt_info0}|{encrypt_info1}\n")


def signup():
    accounts_read()
    print("<-----------------------------------------Kayıt Programı----------------------------------------->")

    mail = input("Mail Adresinizi Giriniz: ")
    for i in accounts:
        while mail == i:
            goback = input("\nGirilen Mail Adresi Halihazırda Kayıtlıdır, Kayıt Olmaya Devam Etmek İçin 'E', Programa Geri Dönmek İçin 'Q' Tuşlayınız: ").upper()
            if goback == "E":
                mail = input("\nMail Adresinizi Giriniz: ")
            else:
                return False
    while "@" not in mail:
        print("Geçerli Bir Mail Adresi Girmeniz Gerekmektedir!")
        mail = input("Mail Adresinizi Giriniz: ")

    new_user = input("Kullanıcı Adı: ")

    while any(new_user == v[0] for v in accounts.values()):
        print("Girilen Kullanıcı Adı Halihazırda Kullanımdadır, Lütfen Farklı Bir Kullanıcı Adı Seçiniz!")
        new_user = input("Kullanıcı Adı: ")

    trys = 0

    new_pass =  maskpass.askpass("Şifre: ")
    while len(new_pass) < 8 or len(new_pass) > 16:
        print("Oluşturacağınız Şifre En Az 8 En Fazla 16 Karakter Olmalıdır!")
        new_pass = maskpass.askpass("Şifre: ")

    v_new_pass =  maskpass.askpass("Şifrenizi Doğrulayın: ")
    while new_pass != v_new_pass:
        print("Şifreler Eşleşmiyor, Lütfen Doğru Girdiğinize Emin Olunuz!")
        new_pass = maskpass.askpass("Şifre: ")
        v_new_pass = maskpass.askpass("Şifrenizi Doğrulayın: ")
        trys += 1
        if trys == 3:
            print("Çok Sayıda Geçersiz İşlem Yapıldı Program Kapatılıyor...")
            exit()

    accounts.update({mail: [new_user, new_pass]})
    print(f"Sayın Kullanıcı {new_user}, Kaydınız Başarıyla Gerçekleşmiştir!\nPrograma Yönlendiriliyorsunuz...")
    return "Succesful Signup"


def login():
    accounts_read()
    trys = 0
    wrong_pass = 0
    print("<----------Login---------->")
    while True:
        username = input("Kullanıcı Adı : ")
        password = maskpass.askpass("Şifre: ")

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
            elif not any(username == v[0] for v in accounts.values()):
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
    accounts_read()
    print("<-----------Şifremi Unuttum----------->")

    mail = input("Mail Adresiniz: ")
    if mail in accounts:
        username = accounts[mail][0]
        vcode = random.randint(100000, 999999)
        print(vcode)
        # img = qrcode.make(vcode)              # Qr if you want but Works On Python 3.8.2
        # img.show()                            # Qr if you want but Works On Python 3.8.2

        trys = 0
        v_pass = 0
        while trys < 3:
            verify = int(input(f"{mail} Adresine Gelen 6 Haneli Doğrulama Kodunu Giriniz: "))
            if verify == vcode:
                changed_pass = maskpass.askpass("Yeni Şifre: ")
                v_changed_pass = maskpass.askpass("Yeni Şifreyi Doğrulayın: ")
                while changed_pass != v_changed_pass:
                    print("Şifreler Eşleşmiyor, Lütfen Doğru Girdiğinize Emin Olunuz!")
                    changed_pass = maskpass.askpass("Yeni Şifre: ")
                    v_changed_pass = maskpass.askpass("Yeni Şifreyi Doğrulayın: ")
                    v_pass += 1
                    if v_pass == 3:
                        print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
                        exit()

                accounts[mail][1] = changed_pass
                print(f"Sayın Kullanıcı {username}, Şifreniz Başarıyla Değiştirildi!\n")
                return "Succesful Password Change"
            else:
                print("\nGirilen Kod Yanlış!\n")
                trys += 1
        if trys == 3:
            print("Çok Sayıda Yanlış Deneme Yapıldı Program Kapatılıyor!")
            exit()

    elif mail not in accounts:
        print("Bu Mail Adresine Kayıtlı Bir Kullanıcı Bulunmamaktadır!")
        ask_signup = input("Kayıt Olmak İçin 'E', Sisteme Geri Dönmek İçin 'Q' Tuşlayınız (E/Q): ").upper()
        if ask_signup == "E":
            return "Noaccount"
        else:
            return "Again"


while True:
    print("\n<----------- Login System ----------->")

    choice = input("1.Kayıt Ol (Signup)\n2.Giriş Yap (Login)\n3.Şifremi Unuttum (Forgot Password)\n4.Çıkış Yap (Exit)\nSeçiniz: ").capitalize()

    if choice in ["1", "Kayıt ol", "Signup"]:
        signup_result = signup()
        accounts_save()

    elif choice in ["2", "Giriş yap", "Login"]:
        login_result = login()
        if login_result == True:
            exit()

        elif login_result == False:
            print("\nInvalid Argument! You are being redirected to the program...\n")
            continue
        
        elif login_result == "Try Again":
            trys = 0
            while login_result == "Try Again":
                login_result = login()
                if login_result == "Incorrect":
                    changepass()
                    accounts_save()
                elif login_result == True:
                    exit()
                trys += 1
                if trys == 4 :
                    print("\nToo many incorrect attemps! Shutting Down...")
                    exit()
                

        elif login_result == "Incorrect":
            chgpass_result = changepass()
            if chgpass_result == "Noaccount":
                signup_result = signup()
                if signup_result == False:
                    continue
                else:
                    accounts_save()
            elif chgpass_result == "Succesful Password Change":
                accounts_save()
            else:
                continue

        elif login_result == "Signup":
            signup_result = signup()
            if signup_result == "Succesful Signup":
                accounts_save()
            elif signup_result == "Changepass":
                chgpass_result = changepass()
                if chgpass_result == "Succesful Password Change":
                    accounts_save()
            elif signup_result == False:
                exit()
        else:
            continue

    elif choice in ["3", "Şifremi unuttum", "Forgot password"]:
        chgpass_result = changepass()
        if chgpass_result == "Noaccount":
            signup_result = signup()
            if signup_result == "Succesful Signup":
                accounts_save()
            else:
                continue
        else:
            continue

    elif choice in ["4", "Çıkış yap", "Exit"]:
        print("Çıkış Yapılıyor...")
        exit()

    else:
        print("Invalid Argument! Shutting Down...")
        exit()
