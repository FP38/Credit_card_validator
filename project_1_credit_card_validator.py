# Credit card validator
sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input('Enter credit card number: ')
card_number = card_number.replace('-', '')
card_number = card_number.replace(' ', '')
card_number = card_number[::-1]

for i in card_number[::2]:
    sum_odd_digits += int(i)

for i in card_number[1::2]:
    i = int(i) * 2
    if i >= 10:
        sum_even_digits += (1 + (i % 10))
    else:
        sum_even_digits += i

total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
    print('VALID')
else:
    print('INVALID')
