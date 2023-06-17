import random

list_of_used_numbers = []

adhaar = random.randint(100000000000, 999999999999)

list_of_used_numbers.append(adhaar)


if adhaar in list_of_used_numbers:
    isRepeat = True
else:
    isRepeat = False

while isRepeat:
    adhaar = random.randint(100000000000, 999999999999)
    if adhaar in list_of_used_numbers:
        isRepeat = True
    else:
        isRepeat = False
        list_of_used_numbers.append(adhaar)
