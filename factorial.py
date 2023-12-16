a = input("Bir Tam Sayi Giriniz")

def faktöriyel(sayi):
    faktöriyel = 1
    for i in range(1,sayi + 1):
        faktöriyel *= i
    print("faktöriyel" , faktöriyel)

while not a.isdigit():  
    print("Bir Tam Sayi Girmeniz Gerekmekte")
    a = input("Bir Tam Sayi Giriniz: ")

a = int(a)
faktöriyel(a)