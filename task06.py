#  6. Telefon raqami operatorini aniqlash
phone = int(input("Telfon raqamni kiriting . " ))
if phone == 90 or phone == 91:
    print("Beeline.")
elif phone == 93 or phone == 94 or phone ==  50 :
    print("Ucell")
elif phone == 99:
    print("Uzmobile")
elif phone == 88:
    print("Mobiuz")
else:
    ("Noma'lum operator")