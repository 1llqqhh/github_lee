#!/bin/python2.7

asnwer = raw_input('您是否是会员y/n')
money = float(input('输入您的购物金额'))

if asnwer == 'y':
    if money >= 200:
        print('打8折，你的金额为：',money * 0.8)
    elif money >= 100 :
        print('打9折，你的金额为：',money * 0.9)
    else:
        print('不打折，你的金额为：',money)
else:
    if money >= 200 :
        print('打95折，你的金额为：', money * 0.95 )
    else:
        print('不打折，你的金额为：', money)

print("welcome next time!!!")
