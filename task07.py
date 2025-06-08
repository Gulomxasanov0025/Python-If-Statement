 #  7. Email manzilini tekshirish
email = input("Email manzilini kiriting: ")

if "@" in email and "." in email and email.find("@") < email.rfind(".") and " " not in email:
    print("Email manzili to'g'ri")
else:
    print("Email manzili noto'g'ri")