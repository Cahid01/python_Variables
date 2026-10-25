#İstifadəçidən şagirdlərin sayını və bir dəftərin qiymətini al. Bütün şagirdlər üçün bir dəftər alındıqda 
#ümumi xərcin nə qədər olacağını hesabla.



student = int(input("Şagirdlərin sayı: "))
price = float(input("Dəftərin qiyməti: "))

total = student * price 
print("Ümumi xərc: ", round(total,1), "AZN")
