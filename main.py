#LISTA E IMPORT DO ARQUIVO PARA CONVERSÃO E ATUALIZAÇÃO

prateleira_de_jogos = []

arquivo = open("arquivo.txt","r")

ler = arquivo.readlines()
for line in ler:
	convert = eval(line)
	prateleira_de_jogos.append(convert)

#######################################################

#FUNÇÕES PARA CHECAGEM DE INPUT

def option_check(input_data): #verifica as opcoes do menu
	if input_data == "1":
		novo_jogo()
	elif input_data == "2":
		ver_tudo()
	elif input_data == "3":
		filtrar_jogos()
	else:
		return voltar_e_sair(input_data)

def check_empty_input(): #checa se o input esta vazio
	while True:
		try:
			entrada = input().upper()

			if len(entrada) > 0 and entrada.isalnum:
				return voltar_e_sair(entrada)
				break

			elif len(entrada) == 0:
				print("Campo não pode ser deixado em branco. Tente novamente.\n")

			else:
				print("Entrada inválida.")

		except EOFError:
			print("Entrada inválida.")
			continue

def check_empty_filter(input_data, input_opt): #identifica se o filtro esta vazio

  while True:
    try:
      if len(input_data) > 0:
        global validade
        validade = True
        return voltar_e_sair(input_data.upper())
        break
      else:
        print("Campo não pode ser deixado em branco.")
        filtrar_jogos(input_opt)
        break

    except AttributeError:
      print("Campo não pode ser deixado em branco.")
      continue

def voltar_e_sair (input_data): #checa se o usuario executou os comandos de retornar ao inicio ou sair
	if input_data == "*":
		start()
	elif input_data == "9":
		print("Salvando e saindo...")
		quit()
	else:
		return input_data

def waiting_for_input():
	while True:
		try:
			option_check(input())
		except EOFError:
			continue

#######################################################

#FUNCAO DE CONTADOR INTERNO PARA FILTRO DE ITENS

def check_results(counter):
	if counter == 0 and validade == True:
		print("\nNenhum resultado encontrado.")
	else:
		return

#######################################################

#FUNCOES DOS MENUS

#TELA INICIAL

def start():
	print(f"""
------------------------------------------------------
------------------- SEJA BEM VINDO -------------------
------------------------------------------------------

    - Para adicionar um novo jogo, digite 1.
    - Para ver todos os jogos, digite 2.
    - Para filtrar seus jogos, digite 3.

                - A qualquer momento -

    - Digite 9 para encerrar o programa.
    - Digite * para voltar ao início.

------------------------------------------------------
------------------------------------------------------
------------------------------------------------------\n""")
	waiting_for_input()

#1 NOVO JOGO

def novo_jogo():

	print("\n------------------------------------------------------")
	print("\n- Digite o nome do jogo:\n")
	jogo = check_empty_input()
	print("\n- Digite o ano de lançamento:\n")
	ano_de_lancamento = check_empty_input()
	print("\n- Digite a plataforma original do jogo:\n")
	plataforma = check_empty_input()
	print("\n- Digite o gênero do jogo:\n")
	genero = check_empty_input()
	prateleira_de_jogos.append({
		"jogo": jogo.upper(),
		"ano de lançamento": ano_de_lancamento,
		"plataforma": plataforma.upper(),
		"genero": genero.upper(),
		})
	with open("arquivo.txt", "w") as file:
		for dados in prateleira_de_jogos:
			file.write(str(dados) + "\n")
	print("\n------------ Jogo adicionado com sucesso! ------------")
	waiting_for_input()

#2 LISTAR JOGOS

def ver_tudo():
	print(f"""
------------------------------------------------------
--------------- PRATELEIRA DE JOGOS ------------------
------------------------------------------------------
""")
	for jogos in prateleira_de_jogos:
		print(f"""
	Nome: {jogos.get("jogo")}
	Ano: {jogos.get("ano de lançamento")}
	Plataforma: {jogos.get("plataforma")}
	Gênero: {jogos.get("genero")}""")
	print(f"""
------------------------------------------------------
-------------------------- Pressione * para voltar ---
------------------------------------------------------
""")

#3 FILTRAR JOGOS

def filtrar_jogos(filtro=False):
  global validade
  validade = False
  if not filtro:
    print(f"""
------------------------------------------------------
---------------- BUSCAR NA PRATELEIRA ----------------
------------------------------------------------------

Gostaria de filtrar seus jogos por:

1 - Ano de lançamento;
2 - Plataforma;
3 - Gênero.

------------------------------------------------------
-------------------------- Pressione * para voltar ---
------------------------------------------------------
\n""")
    while True:
      try:
        filtro = input()

        if filtro == "1":
          counter = 0
          validade = False
          parametro = check_empty_filter(input(f"""
------------------------------------------------------

- Digite o ano de lançamento desejado.        		
	Seus jogos serão listados à seguir:\n\n"""), filtro)
          print("\n------------------------------------------------------")
          for info in prateleira_de_jogos:
            if parametro == info.get("ano de lançamento"):
              counter += 1
              print(f"""
  {info.get("jogo")}""")
          check_results(counter)
          print(f"\n------------------------------------------------------\n\n")

        elif filtro == "2":
          counter = 0
          validade = False
          parametro = check_empty_filter(input(f"""
------------------------------------------------------

- Digite a plafatorma desejada.        		
	Seus jogos serão listados à seguir:\n\n"""), filtro)
          print("\n------------------------------------------------------")
          for info in prateleira_de_jogos:
            if parametro == info.get("plataforma"):
              counter += 1
              print(f"""
	{info.get("jogo")}""")
          check_results(counter)
          print("\n------------------------------------------------------\n\n")

        elif filtro == "3":
          counter = 0
          validade = False
          parametro = check_empty_filter(input(f"""
------------------------------------------------------

- Digite o gênero desejado.
	Seus jogos serão listados à seguir:\n\n"""), filtro)
          print("\n------------------------------------------------------")
          for info in prateleira_de_jogos:
            if parametro == info.get("genero"):
              counter += 1
              print(f"""
	{info.get("jogo")}""")
          check_results(counter)
          print("\n------------------------------------------------------\n\n")

        else:
          filtro = voltar_e_sair(filtro)

      except EOFError:
        continue

#INICIO DO PROGRAMA

input("--- Pressione \'Enter\' para iniciar o programa...")
if True:
	start()