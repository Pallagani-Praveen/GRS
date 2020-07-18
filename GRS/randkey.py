from random import random
from math import floor,ceil
def randnum():
    value = floor(random()*(9200-1200))+1200
    return value

def make_ratings(mobiles):
    for mobile in mobiles:
        strg = ''
        num = 5 - mobile.rating
        for i in range(mobile.rating):
            strg+='1'
        for i in range(num):
            strg+='0'
        mobile.rating = strg
    return mobiles

def genOTP():
    value = floor(random()*(920000-120000))+120000
    return value