def is_latin_word(word):
    for i in word:
        if (ord(i) > 122) or (ord(i) < 97):
            return False
    return True

def int_func(word):
    new_word = []
    if is_latin_word(word):
        new_word = chr(ord(word[0]) - 32) + word[1:]
        return new_word
    else:
        return word

print('Введите строку')
my_str = input()
new_str = ""
for word in my_str.split():
    new_str += int_func(word) + " "

print(new_str)