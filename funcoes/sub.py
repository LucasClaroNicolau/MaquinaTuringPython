import os
def maquina_sub(fita):
    estado = -1
    pos = 0
    while (estado != 8):
        print(estado)
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
            else:
                estado = 6
                pos -= 1

        elif (estado == 3):
            if (fita[pos] == '*'):
                pos -= 1
            else:
                estado = 4
                pos -= 1

        elif (estado == 4):
            if (fita[pos] == '*'):
                pos -= 1
            else:
                estado = 5
                pos += 1

        elif (estado == 5):
            if (fita[pos] == '*'):
                estado = 0
                fita[pos] ='_'
                pos += 1

        elif (estado == 6):
            if (fita[pos] == '*'):
                pos -= 1
            elif(fita[pos] == '_'):
                estado = 7
                fita[pos] = '>'
                pos -= 1
            else:
                estado = 8
                pos += 1

        elif (estado == 7):
            if (fita[pos] == '>'):
                fita[pos] = '_'
                pos += 1
                estado = 8
            else:
                fita[pos] = '_'
                pos -= 1

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
    p = 0;
    for item in range(len(fita)):
        if (fita[item] == '>'):
            break
        p += 1
    for item in range(p):
        fita.remove('_')
    print('Fim')
    print(''.join(fita))
    input()
    return


# -----------------------------------------------------------------------------------------------------

def monta_sub(a,b):
    ret = ['>']
    for item in range(a):
        ret.append('*')
    ret.append('_')

    for item in range(b):
        ret.append('*')
    ret.append('_')
    return ret

# -----------------------------------------------------------------------------------------------------

def mensagem_sub():
    print('Impossivel Subtrair, Primeiro numero é maior que o segundo!\n')
    input()

# -----------------------------------------------------------------------------------------------------
def sub(v1, v2):
    if (v1 < v2):
        mensagem_sub()
    else:
        fita = (monta_sub(v1,v2))
        maquina_sub(fita)
