import random, string
from random import randint

class BaseScript():  

    def randomInputStr(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def randomInputNumb(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)


