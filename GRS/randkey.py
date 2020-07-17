from random import random
from math import floor,ceil
def randnum():
    value = floor(random()*(9200-1200))+1200
    return value

def make_ratings(mobiles):
    for mobile in mobiles:
            point = mobile.rating - floor(mobile.rating)
            if point >= 0.5:
                mobile.rating = ceil(mobile.rating)
            else:
                mobile.rating = floor(mobile.rating)

            mobile.rating = [x for x in range(floor(mobile.rating))]
    return mobiles

def genOTP():
    value = floor(random()*(920000-120000))+120000
    return value