import _thread
import time


def a(msg):
    x = 1
    while x < 2:
        x += 1
        time.sleep(3)
        print(msg)


def b(msg):
    y = 1
    while y < 2:
        y += 1
        time.sleep(5)
        print(msg)


try:
    _thread.start_new_thread(a('thread1'))
    _thread.start_new_thread(b('thread2'))
except:
    print('Error while start')
while 1:
    pass
