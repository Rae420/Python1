def add_range(num1, num2):
    total = 0
    for num1 in range(num1, num2+1):
        total += num1
    print(total)

add_range(3, 20)

print('')

def even_numbers(num1, num2):
    if num2 % 2 != 0:
        print('please supply an even number')
    else:
        while num1 <= num2:
            if num1 % 2 == 0:
                print(num1)
            num1 += 1


var1 = int(input('Enter start number : '))
var2 = int(input('Enter stop number : '))

even_numbers(var1, var2)

