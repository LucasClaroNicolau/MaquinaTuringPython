def maquina_iguala(fita):
    estado = -1
    pos = 0
    while (estado != 8):
        print(estado,pos)
        marc = []
        for i in range(pos):
            marc.append(' ')
        marc.append('|')
        auxmarc = ''.join(marc)
        print('{0} \n'.format(auxmarc))
        aux = ''.join(fita)
        print('{0} \n'.format(aux))
        input()
        if (estado == -1):
            pos += 1
            estado += 1
        elif (estado == 0):
            if fita[pos] == '*':
                estado = 1
                fita[pos] = '$'
                pos += 1
            else:
                estado = 6
                pos += 1
        elif (estado == 1):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 2
                pos += 1
        elif (estado == 2):
            if (fita[pos] == '*'):
                estado = 3
                fita[pos] = '$'
                pos -= 1
            else:
                estado = 4
                pos += 1
        elif (estado == 3):
            if (fita[pos] == '$'):
                estado = 0
                pos += 1
            else:
                pos -= 1
        elif (estado == 4):
            if (fita[pos] == '$'):
                pos += 1
            else:
                estado = 5
                fita[pos] = '$'
                pos -= 1
        elif (estado == 5):
            if (fita[pos] == '$'):
                pos -= 1
            else:
                estado = 3
                pos -= 1
        elif (estado == 6):
            if (fita[pos] == '_'):
                estado = 7
                pos -= 1
            elif(fita[pos] == '*'):
                estado = 6
                fita[pos] = '_'
                pos += 1
            else:
                pos += 1
        elif (estado == 7):
            if (fita[pos] == '$'):
                fita[pos] = '*'
                pos -= 1
            elif (fita[pos] == '_'):
                pos -= 1
            else:
                estado = 8
                pos += 1

    marc = []
    for i in range(pos):
        marc.append(' ')
    marc.append('|')
    auxmarc = ''.join(marc)
    print('{0} \n'.format(auxmarc))
    aux = ''.join(fita)
    print('{0} \n'.format(aux))
    input()
    p = 0;
    for item in range(len(fita)):
        if (fita[item] == '>'):
            break
        p += 1
    for item in range(p):
            fita.remove('_')
    print('Fim \n')
    print(''.join(fita))
    input()
    return


# -----------------------------------------------------------------------------------------------------

def monta_iguala(a,b):
    ret = ['>']
    for item in range(a):
        ret.append('*')

    ret.append('_')

    for item in range(b):
        ret.append('*')
    for item in range(a-b):
        ret.append('_')
    ret.append('_')
    return ret



# -----------------------------------------------------------------------------------------------------
def iguala(v1, v2):

        fita = (monta_iguala(v1,v2))
        maquina_iguala(fita)
