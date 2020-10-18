def get_current_sum(str):
    exit_flag = 1
    current_sum = 0
    for elem in str.split():
        try:
            number = int(elem)
            current_sum += number
        except Exception:
            if (elem == "q"):
                exit_flag = 0
                break
    return [current_sum, exit_flag]

flag = 1
sum = 0
while flag:
    print("Введите строку чисел через пробел: ")
    str = input()
    [current_sum, flag] = get_current_sum(str)
    sum += current_sum
    print(sum)
