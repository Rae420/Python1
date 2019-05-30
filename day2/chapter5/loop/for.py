states = ['Imo', 'Anambra', 'Akwa Ibom', 'Lagos', 'Edo']

for key in states:
    print(key)

print('')

for x in range(1,7):
    print(x)

print('')

states = {
    'Imo': 'Owerri',
    'Lagos': 'Ikeja',
    'Oyo': 'Ibadan',
    'RIvers': 'Port Harcourt',
    'Taraba': 'Yalingo'
}

i = 0
for i in states:
    print(states[i])

print('')

for state in states:
    print(state)

print('')

for state, capital in states.items():
    print(state + ' : '+ capital)

