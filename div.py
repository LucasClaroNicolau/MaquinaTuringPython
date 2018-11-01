def maquina_divi(fita):
    estado = -1
    pos = 0
    while (estado != 21):
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
        elif (estado == 1):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 2
                pos += 1
        elif (estado == 2):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 3
                pos -= 1
        elif (estado == 3):
            if (fita[pos] == '*'):
                estado = 4
                fita[pos] = '$'
                pos -= 1
        elif (estado == 4):
            if (fita[pos] == '*'):
                estado = 5
                pos -= 1
            else:
                estado = 10
                pos += 1
        elif (estado == 5):
            if (fita[pos] == '*'):
                pos -= 1
            elif (fita[pos] == '$'):
                estado = 6
                pos += 1
            else:
                pos -= 1
        elif (estado == 6):
            if (fita[pos] == '*'):
                estado = 7
                fita[pos] = '$'
                pos += 1
            else:
                estado = 12
                pos += 1
        elif (estado == 7):
            if (fita[pos] == '*'):
                pos += 1
            elif (fita[pos] == '$'):
                estado = 3
                pos -= 1
            else:
                estado = 8
                pos += 1
        elif (estado == 8):
            if (fita[pos] == '*'):
                pos += 1
            elif (fita[pos] == '$'):
                estado = 3
                pos -= 1
            else:
                estado = 3
                pos -= 1
        elif (estado == 9):
            if (fita[pos] == '_'):
                estado = 10
                pos += 1
        elif (estado == 10):
            if (fita[pos] == '$'):
                estado = 10
                fita[pos] = '*'
                pos += 1
            else:
                estado = 11
                pos += 1
        elif (estado == 11):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 5
                fita[pos] = '*'
                pos -= 1
        elif (estado == 12):
            if (fita[pos] == '*'):
                pos += 1
            elif (fita[pos] == '$'):
                estado = 13
                pos += 1
            else:
                estado = 20
                fita[pos] = '>'
                pos -= 1
        elif (estado == 13):
            if (fita[pos] == '$'):
                pos += 1
            else:
                estado = 14
                pos += 1
        elif (estado == 14):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 15
                pos += 1
        elif (estado == 15):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 16
                fita[pos] = '*'
                pos -= 1
        elif (estado == 16):
            if (fita[pos] == '>'):
                estado = 18
                pos -= 1
            elif (fita[pos] == '$'):
                estado = 17
                pos -= 1
            else:
                pos -= 1
        elif (estado == 17):
            if (fita[pos] == '*'):
                estado = 18
                pos += 1
            else:
                pos -= 1
        elif (estado == 18):
            if (fita[pos] == '$'):
                estado = 19
                fita[pos] = '*'
                pos += 1
        elif (estado == 19):
            if (fita[pos] == '$'):
                estado = 13
                pos += 1
            else:
                estado = 20
                fita[pos] = '>'
                pos -= 1
        elif (estado == 20):
            if (fita[pos] == '>'):
                estado = 21
                fita[pos] = '_'
                pos += 1
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

def converte_divi(n):
    s = []
    for i in range(n):
        s.append('*')
    return s


# -----------------------------------------------------------------------------------------------------

def monta_divi(a):
    ret = ['>']
    for item in range(len(a)):
        ret.append('*')

    ret.append('_')
    return ret


# -----------------------------------------------------------------------------------------------------
def mensagem_div():
    print('Impossivel Dividir, Primeiro numero é menor que o segundo!\n')
    input();


# -----------------------------------------------------------------------------------------------------
def mensagem_div_zero():
    print('Impossivel Dividir por 0.\n')
    input()


# -----------------------------------------------------------------------------------------------------
def divi(v1, v2):
    if (v2 > v1):
        mensagem_div()
    elif (v2 == 0):
        mensagem_div_zero()
    else:
        fita = (monta_divi(converte_divi(v1)))

        for item in range(v2):
            fita.append('*')
        for item in range(v1):
            fita.append('_')

        maquina_divi(fita)
