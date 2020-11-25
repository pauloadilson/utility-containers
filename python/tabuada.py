tabN = int(input('Informe um número para extrair a tabuada: '))
tab = 0
cont = 0
#for tab in range(11):
while cont < 11:
    print("{} x {} = {}." .format(tabN,cont,tab))
    tab = tabN + tabN*cont
    cont = cont + 1