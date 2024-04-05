import os;
import time;


saldo = 0;
deposito = 0;
extrato = " ";
contador_de_saques = 0;
contador_de_depositos = 0;
resp = 5;
while(resp != 4):
    print("""
            -*-Banco Interprise-*-
        
        Seja bem vindo!
        Escolha uma das opções abaixo:
        [1] Sacar
        [2] Depositar
        [3] Ver extrato
        [4] Sair
    """);
    resp = int(input());
    if(resp == 1):
        if(contador_de_saques < 3):
            saque = float(input("Digite o valor que deseja sacar: "));
        
            if(saldo < saque):
                print("Valor para saque indisponível por falta de saldo.");
                time.sleep(3);
                os.system("cls");
            
            elif((saldo > saque) and (saque <= 500)):
                extrato = extrato +"\n"+ str(saldo) + " - " + str(saque) + "\n";
                saldo = saldo - saque;
                extrato = extrato + "Saldo atual = R$ " + str(saldo) + "\n";
                contador_de_saques = contador_de_saques + 1;
    
                print("Saque realizado.");
                time.sleep(3);
                os.system("cls");
            else:
                print("Valor máximo para saque excedido.Limite máximo para saque igual a R$ 500.00");
                time.sleep(3);
                os.system("cls");
                
        else:
            print("Limite máximo de saques diários atingidos.");
            time.sleep(3);
            os.system("cls");
                
    elif(resp == 2):
        deposito = float(input("Digite o valor que deseja depositar: "));
        
        if(deposito >= 0):
            extrato = extrato + "\n" + str(saldo) + " + " + str(deposito) + "\n";
            saldo = saldo + deposito;
            print("Depósito realizado.");
            extrato = extrato +"Saldo atual = R$ " + str(saldo) + "\n";
            time.sleep(3);
            os.system("cls");
            contador_de_depositos = contador_de_depositos + 1;
            
        else:
            print("Valor digitado inválido.");
            time.sleep(3);
            os.system("cls");

    elif(resp == 3):
        print(extrato);
        time.sleep(12);
        os.system("cls");

    elif(resp == 4):
        print("Encerrando o programa...");