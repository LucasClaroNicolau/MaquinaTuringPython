from iguala import iguala
from div import divi
from mult import mult
import os

def op():
    stop = True
    op = ""
    while(stop):
        os.system("cls")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|      Maquina de Turing      |")
        print("|-----------------------------|")
        print("|      1 - Somar              |")
        print("|      2 - Subtrair           |")
        print("|      3 - Multiplicar        |")
        print("|      4 - Dividir            |")
        print("|      5 - Igualar            |")
        print("|      0 - Sair               |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        op = input()
        if(op.isnumeric()):
            stop = False
        os.system("cls");
    return int(op);


if __name__ == '__main__':
    while(True):
        func = op()
        if(func == 1):
            print("Insira primeiro valor")
            v1 = int(input())
            print("Insira segundo valor:")
            v2 = int(input())
        elif(func == 2):
            print("Insira primeiro valor")
            v1 = int(input())
            print("Insira segundo valor:")
            v2 = int(input())
        elif(func == 3):
            print("Insira primeiro valor")
            v1 = int(input())
            print("Insira segundo valor:")
            v2 = int(input())
            mult(v1,v2)
        elif(func == 4):
            print("Insira primeiro valor")
            v1 = int(input())
            print("Insira segundo valor:")
            v2 = int(input())
            divi(v1,v2)
        elif(func == 5):
            print("Insira primeiro valor")
            v1 = int(input())
            print("Insira segundo valor:")
            v2 = int(input())
            iguala(v1, v2)
        elif(func == 0):
            break




