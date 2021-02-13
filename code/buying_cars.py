from typing import List

def nbMonths(startPriceOld: int, 
             startPriceNew: int, 
             savingperMonth: int, 
             percentLossByMonth: int
             ) -> List[int]:

    bank: int = startPriceOld

    i: int = 0

    while bank < startPriceNew:

        i += 1
        if i % 2 == 0:
            percentLossByMonth += 0.5
        startPriceOld *= (1 - percentLossByMonth/100)
        startPriceNew *= (1 - percentLossByMonth/100)
        bank = i * savingperMonth + startPriceOld

    return [i, round(bank - startPriceNew)]

# print(nbMonths(2000, 8000, 1000, 1.5))
assert(nbMonths(2000, 8000, 1000, 1.5) == [6, 766])
assert(nbMonths(12000, 8000, 1000, 1.5) == [0, 4000])


'''
Best solution

def nbMonths(old, new, saving, percent):
    month = 0
    while old - new + saving * month < 0:
        month += 1
        devalue = (100.0 - percent - 0.5 * (month / 2)) / 100.0
        old *= devalue
        new *= devalue
    return [month, round(old - new + saving * month)]

'''