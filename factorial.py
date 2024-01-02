num = input("Bir Tam Sayi Giriniz: ")

def faktöriyel(sayi):
    faktöriyel = 1
    for i in range(1,sayi + 1):
        faktöriyel *= i
    print(f"{num} sayisinin Faktöriyeli = {faktöriyel}")

while not num.isdigit():  
    print("Bir Tam Sayi Girmeniz Gerekmekte")
    num = input("Bir Tam Sayi Giriniz: ")

num = int(num)
faktöriyel(num)