
import threading


def function1():
    print("thread1")

def function2():
    print("thread2")

th1 = threading.Thread(target=function1)
th2 = threading.Thread(target=function2)

th1.start()
th2.start()

th1.join()
th2.join()

""" Custom class """

mylock = threading.RLock()


class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        with mylock:
            while i < 3:
                letters = "ABC"
                for lt in letters:
                    print(lt)
        i += 1


th1 = MyProcess()
th2 = MyProcess()

th1.start()
th2.start()

th1.join()
th2.join()
