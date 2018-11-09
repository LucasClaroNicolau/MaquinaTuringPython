import os
def maquina_soma(fita):
    estado = -1
    pos = 0
    while (estado != 3):
        marc = []
        for i in range(pos):
            marc.append(' ')
        marc.append('|')
        auxmarc = ''.join(marc)
        print('{0}'.format(auxmarc))
        aux = ''.join(fita)
        print('{0} \n'.format(aux))
        input()
        if (estado == -1):
            pos+= 1
            estado += 1

        elif (estado == 0):
            if (fita[pos] == '*'):
                pos += 1
            else:
                fita[pos] = '*'
                pos += 1
                estado = 1

        elif (estado == 1):
            if (fita[pos] == '*'):
                pos +=1
            else:
                pos -= 1
                estado = 2

        elif (estado == 2):
            if (fita[pos] == '*'):
                fita[pos]='_'
                pos -= 1
                estado = 3

    marc = []
    for i in range(pos):
        marc.append(' ')
    marc.append('|')
    auxmarc = ''.join(marc)
    print('{0} \n'.format(auxmarc))
    aux = ''.join(fita)
    print('{0} \n'.format(aux))
    input()
    os.system('cls')
    print('Fim')
    print(''.join(fita))
    input()
    return


# -----------------------------------------------------------------------------------------------------

def monta_soma(a,b):
    ret = ['>']
    for item in range(a):
        ret.append('*')
    ret.append('_')

    for item in range(b):
        ret.append('*')
    ret.append('_')
    return ret


# -----------------------------------------------------------------------------------------------------
def soma(v1, v2):

        fita = (monta_soma(v1,v2))
        maquina_soma(fita)
