# conversion from roman to arab (from 1 to 3999)


transfer = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}


def to_arab(roman):
    a = None
    arab = 0
    arablist = list()
    for char in roman:
        a = transfer.get(char)
        arablist.append(a)
    print(arablist)
    while arablist:
        try:
            for char in arablist:
                c = arablist.pop(0)
                if c < arablist[0]:
                    d = arablist.pop(0)
                    e = d - c
                    arab += e
                else:
                    arab += c

        except IndexError:
            arab += c
            return arab
    return arab

print(to_arab('MMCCCIX'))
print()



# conversion from arab to roman (from 1 to 3999)


def prevod_tisice(numero):
    if numero in range(1,4):
        t = 'M' * numero
        return t
    
    
def prevod_stovky(numero):
    if numero == 0:
        s = ''
    elif numero in range(1,4):
        s = 'C' * numero
    elif numero == 4:
        s = 'CD'
    elif numero in range(5,9):
        s = 'D' + 'C' * (numero - 5)
    else:
        s = 'CM'
    return s


def prevod_desitky(numero):
    if numero == 0:
        d = ''
    elif numero in range(1,4):
        d = 'X' * numero
    elif numero == 4:
        d = 'XL'
    elif numero in range(5,9):
        d = 'L' + 'X' * (numero - 5)
    else:
        d = 'XC'
    return d


def prevod_jednotky(numero):
    if numero == 0:
        j = ''
    elif numero in range(1,4):
        j = 'I' * numero
    elif numero == 4:
        j = 'IV'
    elif numero in range(5,9):
        j = 'V' + 'I' * (numero - 5)
    else:
        j = 'IX'
    return j


def to_roman(sekvence):
    sekvence = str(sekvence)
    retezec = ''
    if len(sekvence) == 4:
        numero = int(sekvence[0])
        x = prevod_tisice(numero)
        retezec += x
        sekvence = sekvence[1:]
    if len(sekvence) == 3:
        numero = int(sekvence[0])
        x = prevod_stovky(numero)
        retezec += x
        sekvence = sekvence[1:]
    if len(sekvence) == 2:
        numero = int(sekvence[0])
        x = prevod_desitky(numero)
        retezec += x
        sekvence = sekvence[1:]
    if len(sekvence) == 1:
        numero = int(sekvence[0])
        x = prevod_jednotky(numero)
        retezec += x
    return retezec
print(to_roman(1234))
print()

