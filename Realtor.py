import difflib
from time import sleep as wait


real_estate_data = {
    "Usa": {
        "New york": {
            "Residential": {
                "For Rent": [
                    {"location": "Manhattan", "price": 3000, "sellerPhone": 11111111},
                    {"location": "Brooklyn", "price": 2500, "sellerPhone": 22222222},
                ],
                "For Sale": [
                    {"location": "Queens", "price": 500000, "sellerPhone": 33333333},
                    {"location": "Bronx", "price": 400000, "sellerPhone": 44444444},
                ],
            },
            "Commercial": {
                "For Rent": [
                    {"location": "Downtown", "price": 5000, "sellerPhone": 55555555},
                    {"location": "Midtown", "price": 7000, "sellerPhone": 66666666},
                ],
                "For Sale": [
                    {"location": "Harlem", "price": 1000000, "sellerPhone": 77777777},
                    {
                        "location": "Upper East Side",
                        "price": 1200000,
                        "sellerPhone": 88888888,
                    },
                ],
            },
        },
        "Los angeles": {
            "Residential": {
                "For Rent": [
                    {"location": "Hollywood", "price": 3500, "sellerPhone": 99999999},
                    {
                        "location": "Beverly Hills",
                        "price": 4000,
                        "sellerPhone": 10101010,
                    },
                ],
                "For Sale": [
                    {
                        "location": "Downtown LA",
                        "price": 600000,
                        "sellerPhone": 20202020,
                    },
                    {
                        "location": "Santa Monica",
                        "price": 700000,
                        "sellerPhone": 30303030,
                    },
                ],
            },
            "Commercial": {
                "For Rent": [
                    {"location": "Downtown", "price": 6000, "sellerPhone": 40404040},
                    {"location": "Hollywood", "price": 8000, "sellerPhone": 50505050},
                ],
                "For Sale": [
                    {
                        "location": "Beverly Hills",
                        "price": 1500000,
                        "sellerPhone": 60606060,
                    },
                    {
                        "location": "Venice Beach",
                        "price": 1800000,
                        "sellerPhone": 70707070,
                    },
                ],
            },
        },
    },
    #
    "Germany": {
        "Berlin": {
            "Residential": {
                "For Rent": [
                    {"location": "Mitte", "price": 2000, "sellerPhone": 80808080},
                    {"location": "Kreuzberg", "price": 1800, "sellerPhone": 90909090},
                ],
                "For Sale": [
                    {
                        "location": "Prenzlauer Berg",
                        "price": 400000,
                        "sellerPhone": 10101011,
                    },
                    {
                        "location": "Charlottenburg",
                        "price": 500000,
                        "sellerPhone": 11111112,
                    },
                ],
            },
            "Commercial": {
                "For Rent": [
                    {
                        "location": "Friedrichshain",
                        "price": 4000,
                        "sellerPhone": 12121213,
                    },
                    {"location": "Neukölln", "price": 3500, "sellerPhone": 13131314},
                ],
                "For Sale": [
                    {"location": "Kreuzberg", "price": 800000, "sellerPhone": 14141415},
                    {"location": "Mitte", "price": 900000, "sellerPhone": 15151516},
                ],
            },
        },
    },
    #
    "Turkey": {
        "Istanbul": {
            "Residential": {
                "For Rent": [
                    {"location": "Kadikoy", "price": 1500, "sellerPhone": 16161616},
                    {"location": "Besiktas", "price": 2000, "sellerPhone": 17171717},
                ],
                "For Sale": [
                    {"location": "Sariyer", "price": 500000, "sellerPhone": 18181818},
                    {"location": "Taksim", "price": 300000, "sellerPhone": 19191919},
                ],
            },
            "Commercial": {
                "For Rent": [
                    {"location": "Maslak", "price": 13000, "sellerPhone": 20202020},
                    {"location": "Levent", "price": 14500, "sellerPhone": 21212121},
                ],
                "For Sale": [
                    {"location": "Ataşehir", "price": 700000, "sellerPhone": 22222222},
                    {"location": "Kozyatağı", "price": 800000, "sellerPhone": 23232323},
                ],
            },
        },
        "Düzce": {
            "Residential": {
                "For Rent": [
                    {"location": "Merkez", "price": 7500, "sellerPhone": 24242424},
                    {"location": "Akçakoca", "price": 5000, "sellerPhone": 25252525},
                ],
                "For Sale": [
                    {"location": "Merkez", "price": 500000, "sellerPhone": 262626262},
                    {"location": "Akçakoca", "price": 700000, "sellerPhone": 27272727},
                ],
            },
            "Commercial": {
                "For Rent": [
                    {"location": "Merkez", "price": 11000, "sellerPhone": 28282828},
                    {"location": "Gümüşova", "price": 12500, "sellerPhone": 29292929},
                ],
                "For Sale": [
                    {"location": "Gölyaka", "price": 1200000, "sellerPhone": 30303030},
                    {"location": "Çilimli", "price": 1300000, "sellerPhone": 31313131},
                ],
            },
        },
    },
    #
    "France": {
        "Paris": {
            "Residential": {
                "For Rent": [
                    {"location": "Montmartre", "price": 9000, "sellerPhone": 32323232},
                    {"location": "Le Marais", "price": 1100, "sellerPhone": 33333333},
                ],
                "For Sale": [
                    {
                        "location": "Saint-Germain",
                        "price": 600000,
                        "sellerPhone": 34343434,
                    },
                    {
                        "location": "Latin Quarter",
                        "price": 350000,
                        "sellerPhone": 35353535,
                    },
                ],
            },
            "Commercial": {
                "For Rent": [
                    {"location": "La Defense", "price": 5000, "sellerPhone": 36363636},
                    {"location": "Opéra", "price": 5500, "sellerPhone": 37373737},
                ],
                "For Sale": [
                    {"location": "Bercy", "price": 750000, "sellerPhone": 38383838},
                    {"location": "Bastille", "price": 850000, "sellerPhone": 39393939},
                ],
            },
        }
    },
}


formatHelperKeywords = [
    "usa",
    "germany",
    "turkey",
    "new york",
    "los angeles",
    "berlin",
    "istanbul",
    "kiralık",
    "satılık",
    "iş yeri",
    "konut",
    "global",
]


currency = {
    "₺": 33,
    "$": 1,
    "€": 0.93,
    "₽": 92,
    "ك": 0.35,
    "¥": 158,
    "£": 0.85,
}


exchangeData = {
    "Usa": {
        "c": "USD",
        "currency": "$",
        "exchangeRate": 0.92,
    },
    #
    "Germany": {
        "c": "EUR",
        "currency": "€",
        "exchangeRate": 0.92,
    },
    #
    "Turkey": {
        "c": "TRY",
        "currency": "₺",
        "exchangeRate": 33,
    },
    #
    "France": {
        "c": "EUR",
        "currency": "€",
        "exchangeRate": 0.92,
    },
}


def formatHelper(param):
    best_match = difflib.get_close_matches(
        param.lower(), formatHelperKeywords, n=1, cutoff=0.3
    )
    return best_match[0].capitalize() if best_match else None


def calculatePrice(price, country):
    return f"{round(price * exchangeData[country]['exchangeRate'])}{exchangeData[country]['currency']}"


def calcCurrency(money, cur):
    return money * currency.get(cur, 1)


def propertyListings(forSale, order, cur):
    forSale = sorted(forSale, key=lambda x: x["price"], reverse=(order == "bk"))
    for num, item in enumerate(forSale, start=1):
        print(
            f"Seçimlerinize Uygun {num}. Gayrimenkul\n"
            f"-----------------------------\n"
            f"Gayrimenkul Tipi: {item['type']}\n"
            f"Ülke: {item['country']}\n"
            f"Şehir: {item['city']}\n"
            f"İlçe: {item['location']}\n"
            f"Fiyat: {round(calcCurrency(item['price'], cur))}{cur}\n"
            f"İletişim Bilgileri: {item['sellerPhone']}\n"
            f"-----------------------------"
        )
        wait(0.5)
    print(f"Kur Bilgisi $/{cur}: {currency.get(cur, 1)}{cur}")


def main():
    forSale = []
    try:
        country = formatHelper(
            input("Lütfen bir ülke seçin (Örneğin: USA, Germany, Turkey, Global): ")
        )

        if country == "Global":
            try:
                moneyLimit = input("Para Limitini Seçiniz (Üst Limit): ")
                cur = "".join(c for c in moneyLimit if not c.isdigit()).strip()
                money = int("".join(m for m in moneyLimit if m.isdigit()).strip())
                for country, cities in real_estate_data.items():
                    for city, categories in cities.items():
                        for category, transactions in categories.items():
                            if "For Sale" in transactions:
                                for sale in transactions["For Sale"]:
                                    if sale["price"] < money:
                                        forSale.append(
                                            {
                                                "type": category,
                                                "country": country,
                                                "city": city,
                                                "location": sale["location"],
                                                "price": sale["price"],
                                                "sellerPhone": sale["sellerPhone"],
                                            }
                                        )

                order = input(
                    "Sıralama şeklini giriniz büyükten küçüğe (bk) veya küçükten büyüğe (kb) : "
                ).lower()

                propertyListings(forSale, order, cur)

            except ValueError:
                print("Geçersiz Veri Girişi")
            return 0

        city = formatHelper(
            input("Lütfen bir şehir seçin (Örneğin: New york, Berlin, Istanbul): ")
        )
        property_type = formatHelper(
            input("Aradığınız gayrimenkul tipini seçin (Örneğin: İş yeri, Konut): ")
        )
        rent_or_sale = formatHelper(input("Kiralık mı Satılık mı: "))
        order = input(
            "Fiyatları küçükten büyüğe (kb) mi yoksa büyükten küçüğe (bk) mi sıralamak istersiniz? "
        ).lower()

        if None in [country, city, property_type, rent_or_sale]:
            raise ValueError("Geçersiz girişler!")

        property_type = "Residential" if property_type == "Konut" else "Commercial"
        rent_or_sale = "For Rent" if rent_or_sale == "Kiralık" else "For Sale"

        listings = real_estate_data[country][city][property_type][rent_or_sale]
        sorted_listings = sorted(
            listings, key=lambda x: x["price"], reverse=(order == "bk")
        )

        print("\nİşte seçtiğiniz kriterlere uygun bulduğum sonuçlar :) \n")
        for item in sorted_listings:
            print(
                f"Konum: {item['location']}, Fiyat: {calculatePrice(item['price'], country)}, Satıcının Telefon Numarası: {item['sellerPhone']}"
            )

    except ValueError as ve:
        print(f"Hata: {ve}")
    except KeyError:
        print("Veri bulunamadı!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


main()
