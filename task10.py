# 10. Ballar bo‘yicha baho
ball = int(input("Balingizni kiriting. "))
if ball >= 90 and ball <= 100 : 
    print("sizning bahoyingiz. A ")

elif ball >= 80 and ball <= 89:
        print("Sizning baxoyingiz B ")
elif ball >= 70 and ball <= 79 :
    print("Sizning balingiz. C " )
elif ball >=60 and ball <= 69:
    print("Sizni balingiz. D  ")
elif ball >= 0 and ball <=59  : 
    print("Sizning balingiz. F ")
else:
    print("Xato ball")