# 9. Uchburchak turi
a = int(input("1-Birinchi tamonni kiritig. "))
b = int(input("2-Birinchi tamonni kiritig. "))
c = int(input("3-Birinchi tamonni kiritig. "))

if a == b == c:
    print("Teng tomonli")
elif a == b or a == c or b == c:

    print("Teng yonli")
else:
    print("Turli tomonli")