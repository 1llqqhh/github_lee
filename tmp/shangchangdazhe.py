vip = raw_input("are you vip(Y/N):")
money = float(input("input your money:"))
anwser = 'Y'

if vip == anwser:
    if money >= 200:
        pay = money * 0.8
        print("0.8 off", pay)
    elif 50 < money < 200:
        pay = money * 0.95
        print("0.95 off", pay)
    else: 
        print(money)
        print("bu da zhe!")
else:
    if money >= 200:
        pay = money * 0.95
        print("0.95 off", pay)
    else:
        print(money)
        print("bu da zhe!")

