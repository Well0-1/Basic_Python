number = input("Bir Tam Sayi Giriniz")

def faktöriyel(sayi):
    faktöriyel = 1
    for i in range(1,sayi + 1):
        faktöriyel *= i
    print("faktöriyel" , faktöriyel)

while not number.isdigit():  
    print("Bir Tam Sayi Girmeniz Gerekmekte")
    number = input("Bir Tam Sayi Giriniz: ")

number = int()
faktöriyel(a)
