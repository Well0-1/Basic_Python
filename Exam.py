import time 
import tkinter as tk
from tkinter import messagebox

start_time = time.time()
max_time = 300

questions = [
    "Soru 1 :\nreq = input('Çift mi Değil mi')\nif req%2 == 0 \n\tprint('Çift')\nelse:\n\tprint('Tek')\nÇıktısısını Yazınız: ",
    "Soru 2 :\nn = 56.32\nprint(chr(round(n)))\nÇıktısını Yazınız:  ",
    "Soru 3 :\nx,y = 3,4\ny,z = 6,8\nprint(x + y + z)\nÇıktısını Yazınız: ",
    "Soru 4 :\nequation = input('x**2 = 9 ise x kaçtır?')\nif equation == '3' or '-3'\n\tprint('Doğru')\nelse:\n\tprint('Yanlış')\nequationa 5 girdisi verilirse çıktısını yazınız: ",
    "Soru 5 :\nprint(20 + '23' + 5000) ",
]
answers = ["error","8","17","doğru","error"]
chances = 3

name = input("İsminizi Giriniz: ")
surname = input("Soyisminizi Giriniz: ")
mail = input("Mail Adresinizi Giriniz: ")
cv = input("CV'nizi Buraya Kopyalayabilirsiniz: ")
social = input("Github,Linkedin, gibi sosyal medya hesaplarınızı kopyalayabilirsiniz: ")

user_prev = messagebox.askyesno("Mülakat Hakkında","Toplam 5 dakikanız bulunmaktadır. Her soru için 2 kez yanlış cevap verme hakkınız bulunmaktadır. Bir soruda 3 Yanlış yaptığınız takdirde mülakatınız başarısız sayılacaktır, Testi zamanında bitirmek ve internet bağlantısından kullanıcı sorumludur. Devam Etmek için evet'e tıklayınız. Bol Şans! ")
if user_prev == False :
    exit()

start = time.time()   
for i in range(len(questions)) :
    etime = time.time()
    if etime - start > max_time :
        print("Süreniz Dolmuştur! Mülakatınız Başarısız Olarak Sonuçlanmıştır!")
        exit()
    while True :
        question = input(questions[i]).lower()
        if question == answers[i] :
            print("Doğru Cevap")
            chances = 3
            break
        else :
            chances -= 1
            print(f"{chances} Hakkınız Kaldı")
            if chances == 0 :
                print(f"Sayın {name} {surname}, Bu Soruya 3 kez yanlış cevap verdiğiniz için mülakatınız başarısız olarak sonuçlanmıştır.")
                exit()
end = time.time()

print(f"Sayın {name} {surname} Tebrikler! Testi {int((end-start)/60)} dakikada ve başarıyla bitirdiniz. Biz Sizi Ararız.")

# OR # 

import time

quest_answer = {
    "Soru1":"Cevap1",
    "Soru2":"Cevap2",
    "Soru3":"Cevap3",
    "Soru4":"Cevap4",
    "Soru5":"Cevap5",
}
chances = 3

name = input("İsminizi Giriniz: ")
surname = input("Soyisminizi Giriniz: ")
mail = input("Mail Adresinizi Giriniz: ")
cv = input("CV'nizi Buraya Kopyalayabilirsiniz: ")
social = input("Github,Linkedin, gibi sosyal medya hesaplarınızı kopyalayabilirsiniz: ")

start_time = time.time()

for key, value in quest_answer.items() :
    while True :
        question = input(f"{key}: ")
        etime = time.time()
        if question == value :
            chances = 3
            if etime - start_time > 300 :
                print("Süreniz Dolmuştur!")
                exit()
            print("Tebrikler, Doğru Cevap!")
            break
        else :
            chances -= 1 
            print(f"Yanlış Cevap {chances} Hakkınız Kaldı!")
            if chances == 0 :
                print("Bu Soruya Toplamda 3 Kez Yanlış Cevap Verdiğiniz İçin Mülakatınız Başarısız Olarak Sonuçlanmıştır!")
                exit()
    
end_time = time.time()

print(f"Sayın {name} {surname} Tebrikler! Testi {int((end_time-start_time)/60)} dakikada ve başarıyla bitirdiniz. Biz Sizi Ararız.")
