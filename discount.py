#İstifadəçidən məhsulun ilkin qiymətini və endirim faizini al. Endirim məbləğini və məhsulun endirimdən sonrakı qiymətini hesabla.



price = float(input("Ilkin qiyməti daxil edin: "))
percentage = int(input("Endirim faizini daxil edin:  "))
discount = price * percentage / 100
discount_price = price - discount
print("Endirim: " , discount, "AZN")
print("Qiymət: ", discount_price , "AZN")


