from InquirerPy import inquirer
import os
import time
import json
import pygame
import random
import math
pygame.mixer.init()


def limpar_tela():
    os.system("cls" if os.name=="nt" else "clear")

def centralizar(TEXTO):
    largura= os.get_terminal_size().columns
    print(TEXTO.center(largura))

def central_input(_tex):
    largo= os.get_terminal_size().columns
    input(_tex.center(largo))

def perder_dinheiro(dinheiro):

    with open("usuario.json", "r") as rot:
        rogan= json.load(rot)
        rogan["dinheiro"]-= dinheiro

    with open("usuario.json", "w") as coisar:
        json.dump(rogan, coisar)

def ganhar_dinheiro(dinh):
    with open("usuario.json", "r") as rot:
            rogan= json.load(rot)
            rogan["dinheiro"]+= dinh
    
    with open("usuario.json", "w") as coisar:
        json.dump(rogan, coisar)




limpar_tela()
pygame.mixer.music.load("musico.mp3")
pygame.mixer.music.play()
time.sleep(1.5)
centralizar("#===============================================#")
centralizar("banco python 3")
centralizar("#===============================================#")
time.sleep(8)
central_input("aperte enter pra continuar")
limpar_tela()

if not os.path.exists("usuario.json"):
    print("ola, vejo que você é novato")
    time.sleep(2)
    print("sou da equipe de desenvolvimento do banco python 3")
    time.sleep(1.4)
    print("ou pros mais intimos, bp3")
    time.sleep(2)
    print("mas ignorando essas informações, precisamos criar uma senha e uma senha pra sua nova conta bancaria")
    time.sleep(2)
    limpar_tela()
    usuario={
    "nome": input("digite seu nome: "),
    "senha": input("digite sua senha: "),
    "dinheiro": 1000,
    "acoes_ativas": ""
    }
    with open("usuario.json", "w") as arquivo:
        json.dump(usuario, arquivo, indent= 4)
    limpar_tela()
    print("agora vc pode usar de maneira confortavel.")
    time.sleep(2)
    print("voce será redirecionado para o app. e necessitará de senha")
    time.sleep(2)
    print("obrigado por usar o banco B3. vc receberá 1000 bits pra começar")
    time.sleep(2)
    limpar_tela()


with open("usuario.json", "r") as arquivo:
        dados= json.load(arquivo)

senha= ""
while senha != dados["senha"]:
    limpar_tela()
    print("digite sua senha pra entrar no banco")
    senha= input("digite sua senha: ")


limpar_tela()
print("██████╗  ██████╗  ██████╗")
time.sleep(0.5)
print("██╔══██╗ ██╔══██╗ ╚════██╗")
time.sleep(0.5)
print("██████╔╝ ██████╔╝  █████╔╝")
time.sleep(0.5)
print("██╔══██╗ ██╔═══╝   ╚═══██╗")
time.sleep(0.5)
print("██████╔╝ ██║      ██████╔╝")
time.sleep(0.5)
print("╚═════╝  ╚═╝      ╚═════╝")
time.sleep(0.2)
acoes_um= inquirer.select(message="Banco Bp3: escolha sua ação \n",
choices=["verificar saldo", "fazer transferencia", "investir", "verificar boletos","sacar","sair"]).execute()

match acoes_um:
    case "verificar saldo":
        limpar_tela()
        print("selecionado: saldo")
        print("vc sabia que se voce investir 20 bits em peixes ingleses, provavelmente isso nao te \n fará ganhar um bigode? assinado: dev :3")
        time.sleep(4)
        limpar_tela()
        print(f"seu saldo na sua conta atualmente é de: {dados["dinheiro"]} \n")
        input("aperte enter para finalizar a ação")
        print("obrigado")

    case "fazer transferencia":
        limpar_tela()
        lista_de_contatos= ["gary", "shelby", "ronaldo", "outro"]
        resposta= ""
        print("listagem de contatos")
        for item in lista_de_contatos:
            print(item)
        resposta= input("quem vc quer transferir o dinheiro: ")
        if resposta not in lista_de_contatos:
            print("error: favor resetar o app")
        else:
            if resposta != "outro":
                limpar_tela()
                valor= float(input(f"defina quanto vc vai passar, voce tem {dados["dinheiro"]}: "))
                perder_dinheiro(valor)
                print(f"voce passou {valor} para {resposta}, obrigado por usar o banco!")
            else:
                limpar_tela()
                pes= input(f"defina para quem vc vai passar a renda:  ")
                din= float(input(f"defina o quanto vc vai passar, voce tem {dados["dinheiro"]}: "))
                perder_dinheiro(din)
                print(f"voce passou {din} para {pes}. obrigado por usar o banco!")


    





    case "investir":
        limpar_tela()
        opcoes= ["As ações estao disparando! hoje é a melhor oportunidade para altos investimentos", "A bolsa de valores está despencando, cuidado","ações sao uma péssima ideia agora.", "Hoje é um otimo dia para comprar a favoritinha telepixes"]
        menso= random.choice(opcoes)
        print(menso)
        meg= inquirer.select(message="======central de investimentos======", choices=["investir em renda fixa", "investir em renda variavel"]).execute()
        if meg== "investir em renda fixa":
            print("voce decidiu testar a renda fixa e ganhou 0.05 centavos")
            ganhar_dinheiro(0.05)
        elif meg== "investir em renda variavel":
            esq= inquirer.select(message= "escolha as opcoes", choices=["Telepixies","Bitcorp", "Nexonix", "Bytebank", "Bitoil" ]).execute()

            if menso == "As ações estao disparando! hoje é a melhor oportunidade para altos investimentos" or (menso == "Hoje é um otimo dia para comprar a favoritinha telepixes" and esq != "Telepixies"):
                limpar_tela()
                ci= float(input("insira o capital que voce quer investir: "))
                limpar_tela()
                perder_dinheiro(ci)
                print(f"vc investiu {ci} aguarde ate ser processado a analise do mercado...")
                time.sleep(2)
                print(f"empresa: {esq}")
                time.sleep(2)
                print(f"valor inserido: {ci}")
                time.sleep(2)
                print(f"juros mercadológicos: 8% a 15%")
                time.sleep(2)
                a= random.randint(8 , 15)
                b= a / 100
                resultado= ci + (ci * b )
                ganhar_dinheiro(resultado)
                print(f"parabens, vc ganhou {resultado} com {b * 100}% de juros")

            elif opcoes == "Hoje é um otimo dia para comprar a favoritinha telepixes" and esq=="Telepixies":
                limpar_tela()
                ci= float(input("insira o capital que voce quer investir: "))
                perder_dinheiro(ci)
                print(f"vc investiu {ci} aguarde ate ser processado a analise do mercado...")
                time.sleep(2)
                print(f"empresa: {esq}")
                time.sleep(2)
                print(f"valor inserido: {ci}")
                time.sleep(2)
                print(f"juros mercadológicos: 10% a 20%")
                time.sleep(2)
                a= random.randint(10 , 20)
                b= a / 100
                resultado= ci + (ci * b )
                ganhar_dinheiro(resultado)
                print(f"parabens, vc ganhou {resultado} com {b * 100}% de juros")

            elif "A bolsa de valores está despencando, cuidado":
                ci= float(input("insira o capital que voce quer investir: "))
                perder_dinheiro(ci)
                limpar_tela()
                print(f"vc investiu {ci} aguarde ate ser processado a analise do mercado...")
                time.sleep(2)
                print(f"empresa: {esq}")
                time.sleep(2)
                print(f"valor inserido: {ci}")
                time.sleep(2)
                print(f"juros mercadológicos: deplorável")
                time.sleep(2)
                a= random.randint(10 , 20)
                b= math.ceil(a) / 100
                resultado= ci + (ci * b )
                perder_dinheiro(resultado)
                print(f"parabens, vc perdeu {resultado} com {b * 100}% de juros negativos..")
                time.sleep(2)
                print("eu ainda te avisei")
        
    case "verificar boletos":
        limpar_tela()
        print("voce ta livre. pode dormir em paz!")

    case "sacar":
        limpar_tela()
        print("========saque=====")
        saq= float(input("digite o valor de saque: "))
        perder_dinheiro(saq)
        print(f"voce retirou {saq}bits do banco!")

    case "sair":
        limpar_tela()
        print("obrigado por usar o banco B3")
        time.sleep(2)