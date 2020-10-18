from itertools import count, cycle
original_list = []
final_list = []
for element in count(1):
    if element > 10:
        break
    else:
        original_list.append(element)
print(original_list)
count = 0
for elem in cycle(original_list):
    if count >= 2 * len(original_list):
        break
    final_list.append(elem)
    count += 1
print(final_list)