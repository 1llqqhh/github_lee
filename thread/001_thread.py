import threading
import time

def func():
    print("吃饭了 !!!")
    time.sleep(2)

def func1():
    print("睡觉了 !!!")
    time.sleep(2)

def func2():
    print('sum:', sum(range(101)))
    time.sleep(2)

def main():
    t = threading.Thread(target=func)
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t.start()
    t1.start()
    t2.start()

if __name__=="__main__":
    main()
