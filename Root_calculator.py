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
a = float(input("a'yi giriniz: "))
b = float(input("b'yi giriniz: "))
c = float(input("c'yi giriniz: "))

root()
