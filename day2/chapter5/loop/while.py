x = 1

while x <= 10:
    print(x)
    x += 1

print('')

states = ['Imo', 'Anambra', 'Akwa Ibom', 'Lagos', 'Edo']

x = 0

while x < len(states):
    print(states[x])
    x += 1

print('')

# The Break sTatement 
y = 1

while y < 6:
    print(y)
    if y == 3:
        break
    y += 1

print('')

z = 0
while z < 6:
    z += 1
    if z == 3:
        continue
    print(z)