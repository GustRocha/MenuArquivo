# -*- coding: utf-8 -*-

menu = 0

def abrirArquivo():
	nome = raw_input("Digite o nome do arquivo: ")

	arquivo = open(nome)

	return arquivo

def lerArquivo(arquivo):

	linhas = arquivo.readline()

	for linha in linhas:
		print linha.strip()


while menu != 3:

	print "(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3) Sair\n"

	menu = input("Digite a opção desejada: ")

	if menu == 1:

		arquivo = abrirArquivo()

		print "Arquivo aberto com sucesso\n"

	elif menu == 2:
		lerArquivo(arquivo)
		print "Fim do arquivo\n "