#İstifadəçidən bir məhsulun qiymətini və alınacaq məhsulların sayını al. 
# Ümumi qiyməti hesabla. 
# İstifadəçinin verdiyi pul məbləğindən nə qədər pul qalacağını çap et.
price = float(input("Məhsulun qiymətini daxil edin: "))
quantity = int(input(" məhsulun sayını daxil edin: "))
total = price * quantity
print ("Umumi qiymət: ", total,"AZN")
money = float(input("Verilen Pul: "))
print ("Qalan pul: ", money - total, "AZN" )

