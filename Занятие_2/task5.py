rating = [7, 5, 3, 3, 2]
print('Введите новое значение: ')
new = int(input())
position = 0
if new < int(rating[-1]):
    rating.append(new)
else:
    while new <= int(rating[position]):
        position += 1
    rating.insert(position, new)
print(rating)




