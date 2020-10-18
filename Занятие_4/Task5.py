from functools import reduce

def multiplication (prev_elem, elem):
    return prev_elem * elem

list = [element for element in range(100, 1001) if element % 2 == 0]
print(list)
print(reduce(multiplication, list))