vip = raw_input("你是VIP么(Y/N):")
money = float(input("请输入你的购物金额:"))
anwser = 'Y'

if vip == anwser:
    if money >= 200:
        pay = money * 0.8
        print("打8折", pay)
    elif 50 < money < 200:
        pay = money * 0.95
        print("打95折", pay)
    else: 
        print(money)
        print("不打折!")
else:
    if money >= 200:
        pay = money * 0.95
        print("打95折", pay)
    else:
        print(money)
        print("不打折!")

