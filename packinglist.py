from __future__ import print_function
import subprocess


def piscinaString(piscina):
    if piscina:
        return "Com piscina"
    else:
        return "Sem piscina"

def veraoString(verao):
    if verao:
        return 'Verao'
    else: 
        return 'Inverno'

def writeEachList(lista):
    f = open("lista.txt", "a")
    for i in range(len(lista[0])):
        line = lista[0][i].capitalize() + " " + str(lista[1][i]) + '\n'
        f.write(line)
    f.close()

def printEssentials():
    f = open("lista.txt", "a")
    f.write("Essentials: \n")
    for i in one_pieces:
        line = i.capitalize() + '\n'
        f.write(line)
    f.write('\n\nRoupitas:\n')
    f.close()

def writeList(verao, dias, cautela):
    f = open("lista.txt", "w")
    header = "Lista para:\n" + str(dias) + " dias\nNivel de cautela: " + str(cautela) + '\n'+  veraoString(verao) + '\n\n\n'# + #piscinaString(piscina) + '\n\n\n'
    f.write(header)
    f.close()
    printEssentials()
    writeEachList(lista_essenciais)
    if verao:
        writeEachList(verao_lista)
    else:
        writeEachList(inverno_lista)


cautela = input('Qual o nivel de cautela?\n')
dias = input('Quantos dias serao?\n')
verao = input('E verao/tempo quente?\n')
#piscina = input('Ha piscina?\n')

######### LIST ##########

one_pieces = ['carregador android', 'carregador pc', 'carregador telemovel', 'cartas', 'cenas da barba', 'chaves casa', 'chinelos', 'coluna', 'comida para a viagem', 'corta unhas', 'desodorizante', 'escova de dentes', 'filmes no pc', 'fones', 'garrafa de agua', 'gel de banho', 'livro', 'oculos', 'pasta de dentes', 'pc', 'perfume', 'pijama', 'powerbank', 'saco para roupa suja', 'telemovel', 'toalha de banho']

lista_essenciais = [['lentes de contacto', 'boxers', 't-shirts', 'calcas', 'sweats', 'casacos'], [dias + cautela + (dias//5 * cautela), dias + cautela + dias // 4, dias + cautela + dias // 4, 2 + dias // 10, min(dias // 5 + 2, 4), min(dias // 4 + 1, 3)]]

verao_lista = [['protetor solar', 'meias curtas', 'meias longas', 'calcoes', 'calcoes de banho', 'toalha de praia', 'chapeu de praia', 'raquetes', 'repelente'], [1, dias * (max(1, dias//5 * cautela, cautela)), dias//6, min(dias // 6 + 2, 4), min(dias // 6 + 2, 4),  min(dias // 6 + 2, 4), min(2, dias // 3 + 1), 1, 1, 1 ,1]]


inverno_lista = [['meias longas', 'meias para dormir'], [dias + (dias//5 + cautela), 1]]

######## END OF LIST ##########
 
writeList(verao, dias, cautela)

subprocess.Popen(['subl', "lista.txt"])