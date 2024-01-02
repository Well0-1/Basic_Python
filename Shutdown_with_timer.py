import time
import os

# Works With Seconds

sleep_time = int(input("Saniye Cinsinden Bilgisayar kaç saniye sonra kapanmasini istiyorsunuz ? : ")) # Shuts down the computer after as many seconds as the number you enter

for i in range(sleep_time) :
    timer = sleep_time - i 
    time.sleep(1)
    if timer <= 60 :
        print(f"\rBilgisayarınız {timer} saniye sonra kapanacaktır!",end="")
                
os.system("shutdown /s /t 1")

# Minute Version

import time
import os

sleep_time = input("Bilgisayarınız Kaç Dakika Sonra Kapatılsın ? : ") # Shuts down the computer after as many minutes as the number you enter

while not sleep_time.isdigit() :
    print("Bir Tam Sayı Girmeniz Gerekmektedir!")
    sleep_time = input("Bilgisayarınız Kaç Dakika Sonra Kapatılsın ? : ")

sleep_time = int(sleep_time)

for i in range(sleep_time) :
    timer = sleep_time - i 
    if timer <= 5 :
        print(f"Bilgisayarınız {timer} dakika sonra kapanacaktır!")
    time.sleep(60)

print("Shutting Down...")
os.system("shutdown /s /t 1")
