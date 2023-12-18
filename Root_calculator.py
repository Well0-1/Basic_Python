def root():
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("Denklemin Kökü Yoktur")
        
    elif delta == 0 :
        print("Denkleminiz Çift Katlı Köktür!")
        print(-b/2*a)
    
    elif delta > 0 :
        print("1.Kök = " , (-b + delta**0.5)/2*a )
        print("2.Kök = " , (-b - delta**0.5)/2*a )

print("Lüften ax^2 + bx + c Şeklinde olan formülün a,b ve c değerlerini giriniz")
a = input("a'yi giriniz: ")
b = input("b'yi giriniz: ")
c = input("c'yi giriniz: ")
while not a.isdigit():
    print("Bir tam sayi girmeniz gerekmektedir!")
    a = input("a'yi giriniz")
while not b.isdigit():
    print("Bir tam sayi girmeniz gerekmektedir!")
    b = input("b'yi giriniz")
while not c.isdigit():
    print("Bir tam sayi girmeniz gerekmektedir!")
    c = input("c'yi giriniz")
    
a = int(a)
b = int(b)
c = int(c)
sonuc = root()