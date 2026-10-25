#İşçinin aylıq maaşını və bonus məbləğini al. Bonus maaşın üzərinə əlavə edildikdən sonra ümumi gəliri hesabla.



salary = float(input("Aylıq maaşı daxil edin: "))
bonus = float(input("Bonusu daxil edin: "))
total = salary + bonus 
print("Ümumi gəlir: ", round(total, 1) , "AZN")
