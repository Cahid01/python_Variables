#İstifadəçidən ikirəqəmli tam ədəd al və rəqəmlərinin yerini dəyişərək yeni ədəd yarat.
#Məsələn: 42 → 24
#İpucu: // və %


a = int(input("İkirəqəmli tam ədəd daxil edin: "))
b = a // 10
c = a % 10
d = c * 10 + b
print("Yeni ədəd: ", d )
