import os
def maquina_mult(fita):
    estado = -1
    pos = 0
    while (estado != 12):
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
                pos += 1
            else:
                estado = 1
                pos += 1
                
                
        elif (estado == 1):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 2
                pos -= 1
                
        elif (estado == 2):
            if (fita[pos] == '*'):
                estado = 3
                fita[pos] = '&'
                pos -= 1
            elif(fita[pos] == '&'):
                estado = 2
                pos -= 1
            else:
                estado = 10
                pos +=1
                
        elif (estado == 3):
            if (fita[pos] == '*'):
                pos -=1
            elif (fita[pos] == '&'):
                pos -= 1
            else:
                estado = 4
                pos -=1
        
        elif (estado == 4):
            if(fita[pos] == '*'):
                pos-=1
            elif(fita[pos] == '_'):
                estado = 10
                pos+=1
            elif(fita[pos] == '&'):
                estado = 3
                pos-=1
            else:
                estado = 5
                pos+=1
                
        elif (estado == 5):
            if (fita[pos] == '*'):
                estado = 6
                fita[pos] = '$'
                pos += 1
            else:
                estado = 9
                pos -= 1
                
        elif (estado == 6):
            if (fita[pos] == '*'):
                pos+=1
            else:
                estado = 7
                pos += 1
                
        elif (estado == 7):
            if (fita[pos] == '_'):
                estado = 8
                pos += 1
            else:
                pos += 1
                
        elif (estado == 8):
            if (fita[pos] == '*'):
                pos += 1
            else:
                estado = 3
                fita[pos] = '*'
                pos -= 1
                
        elif (estado == 9):
            if (fita[pos] == '>'):
                estado = 0
                pos += 1
            else:
                estado = 9
                fita[pos] = '*'
                pos -=1
                
        elif (estado == 10):
            if (fita[pos] == '_'):
                estado = 11
                fita[pos] = '>'
                pos -= 1
            else:
                pos += 1
                
        elif (estado == 11):
            if (fita[pos] == '>'):
                fita[pos] = '_'
                estado = 12
                pos+=1
            else:
                fita[pos] = '_'
                pos -= 1
        
        print(estado,pos, fita[pos])
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

def monta_mult(a,b):
    ret = ['>']
    for item in range(a):
        ret.append('*')

    ret.append('_')

    for item in range(b):
        ret.append('*')
    
    for item in range(a*b+1):
        ret.append('_')

    return ret


# -----------------------------------------------------------------------------------------------------
def mult(v1, v2):
   
        fita = monta_mult(v1,v2)
        maquina_mult(fita)

