parameters = {
    "Tech": ["Telefon", "Pc", "IPad", "Headphone"],
    "Fashion": ["Dress", "Another Dress", "Pants", "Another Pants", "Shoes"],
    "Accessuar": ["Braclet", "Watch", "Ring", "Necklace", "Hat"],
    "Real_Estate": ["House", "Apartment", "Land", "Cottage", "Condominium"],
    "City": ["İstanbul", "New York", "Düzce", "Minnesota", "Washington"],
}
print("Bulunan Kategoriler")
for i in parameters :
    print(i)
print("Hepsini Görüntülemek İçin 'All' ")

while True :
    requested_parameter = input("Görüntülemek istediğiniz kategori: ").lower()
    if requested_parameter == "all":
        for sayi, (key, value) in enumerate(parameters.items(), start=1):                
            print(f"{sayi}-){key} kategorisinde bulunan ürünler: {', '.join(value)}")
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    elif requested_parameter == "tech":
        print("Tech Kategorisinde bulunan ürünler:", ", ".join(parameters["Tech"]))
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    elif requested_parameter == "fashion":
        print("Fashion Kategorisinde bulunan ürünler:", ", ".join(parameters["Fashion"]))
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    elif requested_parameter == "accessuar":
        print("Accessuar Kategorisinde bulunan ürünler:", ", ".join(parameters["Accessuar"]))
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    elif requested_parameter == "real estate":
        print("Real Estate Kategorisinde bulunan ürünler:", ", ".join(parameters["Real_Estate"]))
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    elif requested_parameter == "city":
        print("City Kategorisinde bulunan ürünler:", ", ".join(parameters["City"]))
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    else:
        print("Geçerli Bir Değer Girmeniz Gerekmektedir! ")
        loop = input("Programi Bitirmek İstiyor musunuz? (E/H)").upper()
    if loop == "E":
        print("Program Kapatiliyor...")
        break