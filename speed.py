#İstifadəçidən gedilən məsafəni (km) və sərf olunan vaxtı (saat) al. Orta sürəti hesabla.
#ipucu: Sürət = məsafə / vaxt.


distance = float(input("Gedilen mesafe (KM) : "))
hour = float(input("Serf olun vaxt (SAAT) : "))
speed = distance // hour 
print ("Suret: ", speed, "km/h")

