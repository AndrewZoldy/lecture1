import string

basis = input()
numbers = [input().upper(), input().upper()]
new_basis = input()
digit_list = ''.join([str(i) for i in range(0, 10)]) + string.ascii_uppercase
def convert_to_basis(number, to_basis = 10, from_basis = 10):
    digit_list = ''.join([str(i) for i in range(0, 10)]) + string.ascii_uppercase
    decimal = sum([((digit_list.index(digit[1])) * (int(from_basis) ** digit[0]))
                   for digit in enumerate(str(number)[::-1])])
    if decimal // int(to_basis) == 0:
        return digit_list[decimal]
    else:
        return convert_to_basis(decimal // int(to_basis), int(to_basis)) + digit_list[decimal % int(to_basis)]

print(convert_to_basis(int(convert_to_basis(numbers[0], 10, basis)) +
                       int(convert_to_basis(numbers[1], 10, basis)), new_basis))