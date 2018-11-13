import os
import platform

def limpa():
    plata = platform.system()
    limpa = ""
    if(plata == "Windows"):
        os.system('cls')
    else:
        os.system('clear')


def maquina_iguala(fita):
    estado = -1
    pos = 0
    while (estado != 9):
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
            pos += 1
            estado += 1
        elif (estado == 0):
            if fita[pos] == '*':
                estado = 1
                fita[pos] = '$'
                pos += 1
            else:
                estado = 7
                pos +=1


        elif (estado == 1):
            if (fita[pos] == '*'):
                pos += 1
                estado = 2;
            else:
                estado = 6
                pos += 1


        elif (estado == 2):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 3
                pos += 1


        elif (estado == 3):
            if (fita[pos] == '*'):
                estado = 4
                fita[pos] = '$'
                pos -= 1
            elif(fita[pos] == '$'):
                pos += 1
            else:
                estado = 4
                fita[pos] = '$'
                pos -= 1


        elif (estado == 4):
            if (fita[pos] == '*'):
                estado = 5
                pos -= 1
            else:
                pos -= 1


        elif (estado == 5):
            if (fita[pos] == '$'):
                estado = 0
                pos += 1
            else:
                pos -= 1



        elif (estado == 6):
            if (fita[pos] == '$'):
                pos += 1
            else:
                estado = 7
                fita[pos] = '$'
                pos += 1


        elif (estado == 7):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 8
                pos -= 1

        elif (estado == 8):
            if (fita[pos] == '>'):
                estado = 9
                pos += 1
            elif (fita[pos] == '$'):
                fita[pos] = '*'
                pos -= 1
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
    limpa()
    print('Fim ')
    print(''.join(fita))
    input()
    return


# -----------------------------------------------------------------------------------------------------

def monta_iguala(a, b):
    ret = ['>']
    for item in range(a):
        ret.append('*')

    ret.append('_')

    for item in range(b):
        ret.append('*')
    if (b != 0):
        for item in range(a - b + 1):
            ret.append('_')
    else:
        for item in range(a):
            ret.append('_')
    ret.append('_')
    return ret


# -----------------------------------------------------------------------------------------------------
def iguala(v1, v2):
    fita = (monta_iguala(v1, v2))
    maquina_iguala(fita)
