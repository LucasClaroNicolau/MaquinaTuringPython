from iguala import iguala
from div import divi
from mult import mult
from soma import soma
from sub import sub
import os
def op():
    stop = True
    op = ""
    while(stop):
        os.system("cls")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                                                                                                                                       |")
        print("|                 $$$$$$$$$$$$$$$$$    $$$$$      $$$$$    $$$$$$$$$$$$    $$$$    $$$$$        $$$$     $$$$$$$$$$$$$$$$               |")
        print("|                 $$$$$$$$$$$$$$$$$    $$$$$      $$$$$    $$$       $$    $$$$    $$$$$$       $$$$     $$$$                           |")
        print("|                       $$$$$          $$$$$      $$$$$    $$$       $$    $$$$    $$$$  $$     $$$$     $$$$                           |")
        print("|                       $$$$$          $$$$$      $$$$$    $$$       $$    $$$$    $$$$   $$    $$$$     $$$$                           |")
        print("|                       $$$$$          $$$$$      $$$$$    $$$$$$$$$$$$    $$$$    $$$$    $$   $$$$     $$$$    $$$$$$$$               |")
        print("|                       $$$$$          $$$$$      $$$$$    $$$   $$$       $$$$    $$$$     $$  $$$$     $$$$        $$$$               |")
        print("|                       $$$$$          $$$$$      $$$$$    $$$    $$$      $$$$    $$$$      $$ $$$$     $$$$        $$$$               |")
        print("|                       $$$$$           $$$$      $$$$     $$$     $$$     $$$$    $$$$       $$$$$$     $$$$        $$$$               |")
        print("|                       $$$$$             $$&&&&&&$$       $$$      $$$    $$$$    $$$$        $$$$$     $$$$$$$$$$$$$$$$               |")
        print("|                                                                                                                                       |")
        print("|      $$$$$       $$$$$    $$$$$$$$$$$$$$$    $$$$$$$$$$$$    $$$$        $$$$    $$$$      $$$$$        $$$$     $$$$$$$$$$$$$$$$     |")
        print("|      $$$$ $     $ $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$$$       $$$$     $$$$                 |")
        print("|      $$$$  $   $  $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$  $$     $$$$     $$$$                 |")
        print("|      $$$$   $ $   $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$   $$    $$$$     $$$$                 |")
        print("|      $$$$    $    $$$$    $$$$$$$$$$$$$$$    $$$$            $$$$$$$$$$$$$$$$    $$$$      $$$$    $$   $$$$     $$$$$$$$$$$$$$$$     |")
        print("|      $$$$         $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$     $$  $$$$     $$$$                 |")
        print("|      $$$$         $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$      $$ $$$$     $$$$                 |")
        print("|      $$$$         $$$$    $$$$       $$$$    $$$$            $$$$        $$$$    $$$$      $$$$       $$$$$$     $$$$                 |")
        print("|      $$$$         $$$$    $$$$       $$$$    $$$$$$$$$$$$    $$$$        $$$$    $$$$      $$$$        $$$$$     $$$$$$$$$$$$$$$$     |")
        print("|                                                                                                                                       |")
        print("|                                                                                                                                       |")
        print("|\t\t\t\t\t\t\t1 - Somar       \t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t2 - Subtrair    \t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t3 - Multiplicar \t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t4 - Dividir     \t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t5 - Igualar     \t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t0 - Sair        \t\t\t\t\t\t\t\t\t|")
        print("|                                                                                                                                       |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        op = input()
        if(op.isnumeric()):
            stop = False
        os.system("cls");
    return int(op);


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
                os.system('cls')
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                os.system('cls')
            soma(int(v1),int(v2))
        elif(func == 2):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                os.system('cls')
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                os.system('cls')
            sub(int(v1),int(v2))
        elif(func == 3):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                os.system('cls')
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                os.system('cls')
            mult(int(v1),int(v2))
        elif(func == 4):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                os.system('cls')
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                os.system('cls')
            divi(int(v1),int(v2))
        elif(func == 5):
            while (stop):
                print("Insira o primeiro valor")
                v1 = input()
                if (v1.isnumeric()):
                    stop = False
                os.system('cls')
            stop = True
            while (stop):
                print("Insira o segundo valor")
                v2 = input()
                if (v2.isnumeric()):
                    stop = False
                os.system('cls')
            iguala(int(v1),int(v2))
        elif(func == 0):
            break




