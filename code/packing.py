from typing import List
from rectpack import float2dec, newPacker

class Rectangle:
    def __init__(self, length = 1.2, width = 0.8):
        # дефолтные значения 1.2м3 и 0.8м3 для паллеты если габариты не указаны
        self.length = length
        self.width = width

    def __str__(self):
        return f"l: {self.length}, w: {self.width}"

    def get_volume(self):
        return self.length * self.width

def check_packing(rectangle_list: List[Rectangle], 
                  container: Rectangle, fix_point = 3) -> bool:
    '''
    rectangle_list: List[Rectangle] - список прямоугольников с указанием ширины и длины
    container: Rectangle - ширина и длина транспорта
    fix_point = 3 - для фиксации точки после запятой
    '''

    # проверяем, помещается ли вообще суммарная площадь грузов в транспорт
    items_volume = sum([r.get_volume() for r in rectangle_list])

    if items_volume > container.get_volume():
        return False

    rectangles = [(float2dec(r.length, fix_point), 
                   float2dec(r.width, fix_point)) for r in rectangle_list]

    bins = [(float2dec(container.length, fix_point), 
             float2dec(container.width, fix_point))]

    packer = newPacker()

    # Add the rectangles to packing queue
    for r in rectangles:
        packer.add_rect(*r)

    # Add the bins where the rectangles will be placed
    for b in bins:
        packer.add_bin(*b)

    # Start packing
    packer.pack()

    if len(packer) == 0:
        return False
    if len(packer[0]) != len(rectangles):
        return False

    return True


r1 = Rectangle(2,1)
r2 = Rectangle(2,2)
r3 = Rectangle(3,1)
r4 = Rectangle(1.2,1.1)
r5 = Rectangle(2.1,2.1)
r6 = Rectangle()

c1 = Rectangle(3, 2)
c2 = Rectangle(3, 3)
c3 = Rectangle(3.3, 2.2)
c4 = Rectangle(2.9, 2.9)

assert(check_packing([r1,r2], c1) == True)
assert(check_packing([r1,r2], c2) == True)
assert(check_packing([r1,r2,r3], c1) == False)
assert(check_packing([r1,r2,r3], c2) == True)
assert(check_packing([r2,r2], c2) == False)
assert(check_packing([r1,r3,r3], c2) == True)
assert(check_packing([r1,r4], c2) == True)
assert(check_packing([r5,r5], c2) == False)
assert(check_packing([r6,r6], c1) == True)
assert(check_packing([r6,r6,r6,r6,r6,r6,r6], c1) == False)