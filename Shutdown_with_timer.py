import time
import os

sleep_time = int(input("Saniye Cinsinden Bilgisayar kaç saniye sonra kapanmasini istiyorsunuz ? : "))

for i in range(sleep_time) :
    timer = sleep_time - i 
    time.sleep(1)
    if timer <= 30 :
        print(timer)
                
os.system("shutdown /s /t 1")