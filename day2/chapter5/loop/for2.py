


# for i in score:
#     multiplication = 'x' + score
#     result = score * i
#     print(score + multiplication + result)
#     i += 1



for i in range(1, 13):
    print('2 x', i, ' = ', 2*i)

print('')

x = 1
total = 0

for x in range(31):
    total += x

print(total)

print('')

x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1
