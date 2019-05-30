def Presideny(run):

    contestant = ['Buhari', 'Atiku', 'Sowore', 'Donald Duke']
    run = input('Find out who is contesting for president : ').capitalize()

    if run in contestant:
        print(run + ' is contesting for Presidency' )
    else:
        print(run + ' is not contesting for Pesidency')

        for run in contestant:
        print(run)

