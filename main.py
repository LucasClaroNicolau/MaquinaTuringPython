from funcoes.iguala import iguala
from funcoes.div import divi
from funcoes.mult import mult
from funcoes.soma import soma
from funcoes.sub import sub
import os
import platform

def limpa():
    plata = platform.system()
    limpa = ""
    if(plata == "Windows"):
        os.system('cls')
    else:
        os.system('clear')


def op():
    stop = True
    op = ""
    while(stop):
        limpa()
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                                                                            |")
        print("|     $$$$$$$$$$$   $$       $$   $$$$$$$   $$   $$$     $$   $$$$$$$$$      |")
        print("|         $$        $$       $$   $$    $$  $$   $$$     $$   $$             |")
        print("|         $$        $$       $$   $$$$$$$   $$   $$ $$$  $$   $$             |")
        print("|         $$        $$       $$   $$ $$     $$   $$   $$ $$   $$  $$$$$      |")
        print("|         $$         $$     $$    $$  $$    $$   $$     $$$   $$     $$      |")
        print("|         $$          $$$$$$$     $$   $$   $$   $$     $$$   $$$$$$$$$      |")
        print("|                                                                            |")
        print("| $$$    $$$   $$$$$$$$$   $$$$$$$$$   $$     $$   $$   $$$    $$   $$$$$$$$ |")
        print("| $$ $  $ $$   $$     $$   $$          $$     $$   $$   $$$$   $$   $$       |")
        print("| $$  $$  $$   $$     $$   $$          $$     $$   $$   $$ $$  $$   $$$$$$   |")
        print("| $$      $$   $$$$$$$$$   $$          $$$$$$$$$   $$   $$  $$ $$   $$       |")
        print("| $$      $$   $$     $$   $$          $$     $$   $$   $$    $$$   $$       |")
        print("| $$      $$   $$     $$   $$$$$$$$$   $$     $$   $$   $$    $$$   $$$$$$$$ |")
        print("|                                                                            |")
        print("|  \t\t\t       1 - Somar              \t\t\t     |")
        print("|  \t\t\t       2 - Subtrair           \t\t\t     |")
        print("|  \t\t\t       3 - Multiplicar        \t\t\t     |")
        print("|  \t\t\t       4 - Dividir            \t\t\t     |")
        print("|  \t\t\t       5 - Igualar            \t\t\t     |")
        print("|  \t\t\t       0 - Sair               \t\t\t     |")
        print("|                                                                            |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        op = input()
        if(op.isnumeric()):
            stop = False
            limpa()
    return int(op)


if __name__ == '__main__':
    while(True):
        func = op()
        stop = True
        v1 = ''
        v2 = ''
        if(func == 1):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                limpa()
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                limpa()
            soma(int(v1),int(v2))
        elif(func == 2):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                limpa()
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                limpa()
            sub(int(v1),int(v2))
        elif(func == 3):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                limpa()
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                limpa()
            mult(int(v1),int(v2))
        elif(func == 4):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                limpa()
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                limpa()
            divi(int(v1),int(v2))
        elif(func == 5):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                limpa()
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                limpa()
            iguala(int(v1),int(v2))
        elif(func == 0):
            break




