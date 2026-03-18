narxi = 100.000

yosh = int(input("Yosh kiriting ; "))

if 17 >= yosh >=7:
    sale = yosh + (yosh * 20) / 100
    print(f"Yakuniy narx: {sale} so'm (20% chegirma qo'llanildi)")
elif yosh <= 6:
    sale = yosh + (yosh * 50) / 100
    print(f"Yakuniy narx: {sale} so'm (50% chegirma qo'llanildi)")
elif yosh >= 18:
    sale = yosh + (yosh * 30) / 100
    print(f"Yakuniy narx: {sale} so'm (30% chegirma qo'llanildi)")