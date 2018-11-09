from iguala import iguala
import os

def op():
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
    os.system("cls");
    return op;


if __name__ == '__main__':
    print("antes")
    while(True):
        func = op()
        print("Insira primeiro valor")
        v1 = input()
        print("Insira segundo valor:")
        v2 = input()
        if(func == 1):
            print("1")
        elif(func ==2):
            print("2")
        if(func == 3):
            print("3")
        if(func == 4):
            print("4")
        if(func == 5):
            iguala(v1, v2)
        if(func == 0):
            break




