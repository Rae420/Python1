name = input('Find out who is contesting for president : ').capitalize()

contestant = ['Buhari', 'Atiku', 'Sowore', 'Donald Duke']

if name in contestant:
    print(name + ' is contesting for Presidency' )
else:
    print(name + ' is not contesting for Pesidency')

    for name in contestant:
        print(name)