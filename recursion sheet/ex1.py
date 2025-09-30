import time


def countdown(n):
    if n==0:
        return "BOOM"
    else:
        print(n)
        time.sleep(1)
        return countdown(n-1)
buttler=10
print(countdown(buttler))
