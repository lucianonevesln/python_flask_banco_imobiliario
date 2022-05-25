# ferramentas necessarias
import random
import pandas as pd
from random import randint
from datetime import datetime

# funcao para ser chamada e executada pelo servidor
def executa_programa():
    # funcao para trechos grandes que se repetiam
    def tratamento_lista_vazia():
        # pagamento pela aquisicao da propriedade
        jogadores[jogador] -= propriedades[indice+sorteio_dado]\
                                          [indice+sorteio_dado]\
                                          ["custo_venda"]
        # insere comprado na propriedade
        propriedades[indice+sorteio_dado][indice+sorteio_dado]\
                    ["proprietario"].append(jogador)


    # Tabuleiro do Jogo: dicionario de propriedades com atributos e valores
    propriedades = [
        {0: {
            "custo_venda": 100,
            "valor_aluguel": 50,
            "proprietario": []
        }},
        {1: {
            "custo_venda": 200,
            "valor_aluguel": 100,
            "proprietario": []
        }},
        {2: {
            "custo_venda": 300,
            "valor_aluguel": 150,
            "proprietario": []
        }},
        {3: {
            "custo_venda": 400,
            "valor_aluguel": 200,
            "proprietario": []
        }},
        {4: {
            "custo_venda": 500,
            "valor_aluguel": 250,
            "proprietario": []
        }},
        {5: {
            "custo_venda": 400,
            "valor_aluguel": 200,
            "proprietario": []
        }},
        {6: {
            "custo_venda": 300,
            "valor_aluguel": 150,
            "proprietario": []
        }},
        {7: {
            "custo_venda": 200,
            "valor_aluguel": 100,
            "proprietario": []
        }},
        {8: {
            "custo_venda": 100,
            "valor_aluguel": 50,
            "proprietario": []
        }},
        {9: {
            "custo_venda": 50,
            "valor_aluguel": 25,
            "proprietario": []
        }},
        {10: {
            "custo_venda": 40,
            "valor_aluguel": 20,
            "proprietario": []
        }},
        {11: {
            "custo_venda": 60,
            "valor_aluguel": 30,
            "proprietario": []
        }},
        {12: {
            "custo_venda": 80,
            "valor_aluguel": 40,
            "proprietario": []
        }},
        {13: {
            "custo_venda": 100,
            "valor_aluguel": 50,
            "proprietario": []
        }},
        {14: {
            "custo_venda": 800,
            "valor_aluguel": 400,
            "proprietario": []
        }},
        {15: {
            "custo_venda": 900,
            "valor_aluguel": 450,
            "proprietario": []
        }},
        {16: {
            "custo_venda": 700,
            "valor_aluguel": 350,
            "proprietario": []
        }},
        {17: {
            "custo_venda": 600,
            "valor_aluguel": 300,
            "proprietario": []
        }},
        {18: {
            "custo_venda": 900,
            "valor_aluguel": 450,
            "proprietario": []
        }},
        {19: {
            "custo_venda": 200,
            "valor_aluguel": 100,
            "proprietario": []
        }}
    ]


    # listas para contabilizacao dos resultados
    lista_hora = []
    lista_vencedor = []
    lista_perdedor = []
    lista_comportamento_vencedor = []
    lista_time_out = []


    # for para limitar o numero de partidas a 300
    for partida in range(0, 299):

        # registro da hora de inicio da execucao do programa
        hora_inicial = datetime.today()

        # dicionario com a pontuacao inicial de cada participante do jogo
        jogadores = {
            "jogador_1_impulsivo": 300,
            "jogador_2_exigente": 300,
            "jogador_3_cauteloso": 300,
            "jogador_4_aleatorio": 300
        }

        # sorteia e cria lista com a ordem de cada jogador na partida
        sorteio_sequencia_jogador = random.sample(jogadores.keys(), k=4)

        # contador de partidas para o caso de nao haver vencedor
        contador_partidas = 1

        # for para controlar a vez de cada jogador na partida
        for jogador_sorteado in sorteio_sequencia_jogador:

            # verifica time out
            if contador_partidas < 1000:

                # estrutura para acessar cada jogador em dicionario de jogadores
                for jogador in jogadores:

                    # condicional para verificar se jogador sorteado da vez e o mesmo do
                    # dicionario jogadores, possibilitando a manipulacao de valores que
                    # pertencem ao jogador correto
                    if jogador == jogador_sorteado:

                        # sorteio de casas que o jogador podera percorrer
                        sorteio_dado = randint(1,6)

                        # estrutura para percorrer indices em propriedades
                        for indice in range(0, len(propriedades)):

                            # condicional para verificar se o jogador completou percurso
                            if indice+sorteio_dado <= 19:

                                # sorteio para jogador aleatorio definir sua compra
                                cinquenta_porcento = random.choice([True, False])

                                # condicional para verificar se a posicao definida pelo dado
                                # esta vazia
                                if propriedades[indice+sorteio_dado][indice+sorteio_dado]\
                                               ["proprietario"] == []:

                                    # condicional para validar e executar requisitos do jogador
                                    # impulsivo
                                    if jogador == "jogador_1_impulsivo" and propriedades[indice+sorteio_dado]\
                                       [indice+sorteio_dado]["custo_venda"] <= jogadores[jogador]:
                                        tratamento_lista_vazia()

                                    # condicional para validar e executar requisitos do jogador exigente
                                    elif jogador == "jogador_2_exigente" and propriedades[indice+sorteio_dado]\
                                         [indice+sorteio_dado]["valor_aluguel"] > 50 and\
                                         propriedades[indice+sorteio_dado]\
                                         [indice+sorteio_dado]["custo_venda"] <= jogadores[jogador]:
                                        tratamento_lista_vazia()

                                    # condicional para validar e executar requisitos do jogador cauteloso
                                    elif jogador == "jogador_3_cauteloso" and jogadores[jogador] -\
                                         propriedades[indice+sorteio_dado][indice+sorteio_dado]["custo_venda"] > 80 and\
                                         propriedades[indice+sorteio_dado][indice+sorteio_dado]["custo_venda"] <=\
                                         jogadores[jogador]:
                                        tratamento_lista_vazia()

                                    # condicional para validar e executar requisitos do jogador aleatorio
                                    elif jogador == "jogador_4_aleatorio" and propriedades[indice+sorteio_dado]\
                                         [indice+sorteio_dado]["custo_venda"] <= jogadores[jogador] and\
                                         cinquenta_porcento:
                                        tratamento_lista_vazia()

                                else:

                                    # for para percorrer todos os proprietarios em propriedades
                                    for dono_propriedade in propriedades[indice+sorteio_dado][indice+sorteio_dado]\
                                        ['proprietario']:

                                        # pagamento de aluguel ao proprietario
                                        jogadores[jogador] -= propriedades[indice+sorteio_dado][indice+sorteio_dado]\
                                        ['valor_aluguel']

                                        # ocupacao da propriedade pelo locador
                                        propriedades[indice+sorteio_dado][indice+sorteio_dado]\
                                        ["proprietario"].append(jogador)

                                        # for para recebimento de aluguel pelo proprietario
                                        for recebedor_aluguel in jogadores:

                                            # condicional para identificacao do proprietario
                                            if recebedor_aluguel == propriedades[indice+sorteio_dado]\
                                               [indice+sorteio_dado]\
                                               ['proprietario'][0]:

                                                # recebimento de aluguel pelo proprietario
                                                jogadores[recebedor_aluguel] += propriedades[indice+sorteio_dado]\
                                                         [indice+sorteio_dado]['valor_aluguel']

                                            # for para eliminar jogador com pontuacao abaixo de 0
                                            for jogador_abaixo_0 in jogadores:

                                                # condicionar que valida se a pontuacao esta abaixo de 0
                                                if jogadores[jogador_abaixo_0] < 0:

                                                    # insere perdedor em lista
                                                    lista_perdedor.append(jogador_abaixo_0)

                                        break
                                    
                            else:

                                # pagamento por percurso completado
                                jogadores[jogador] += 100

            # adiciona o principal pontuador em lista
            lista_vencedor.append(max(jogadores))
            # adiciona o principal pontuador em lista de comportamento
            lista_comportamento_vencedor.append(max(jogadores))
            # iteracao de contador_partidas
            contador_partidas += 1

        else:
            # adicionando time_out em lista para contabilizacao
            lista_time_out.append(contador_partidas)

        # registro da hora de finalizacao da execucao do programa
        hora_final = datetime.today()

        # inserindo hora em lista
        lista_hora.append(hora_final-hora_inicial)

    # tratamentos para apresentacao de resultados
    lista_hora = pd.DataFrame(lista_hora, columns = ['Tempo_Medio'])
    lista_vencedor = pd.DataFrame(lista_vencedor, columns = ['Vencedor'])
    lista_perdedor = pd.DataFrame(lista_perdedor, columns = ['Perdedor'])
    lista_comportamento_vencedor = pd.DataFrame(lista_comportamento_vencedor, columns = ['Comportamento'])

    # saida em html
    html_lista_hora = lista_hora.mean()
    html_lista_vencedor = lista_vencedor.groupby(['Vencedor']).value_counts()
    html_lista_perdedor = lista_perdedor.groupby(['Perdedor']).value_counts()
    html_lista_comportamento_vencedor = lista_comportamento_vencedor.groupby(['Comportamento']).value_counts()
    html_lista_time_out = len(lista_time_out)
    
    # saida em console
    print('\n---------------------------------------\n')
    print('---------- Média de Tempo -------------')
    print('\n---------------------------------------\n')
    print(html_lista_hora)

    print('\n---------------------------------------\n')
    print('---------- Vencedores -----------------')
    print('\n---------------------------------------\n')
    print(html_lista_vencedor)

    print('\n---------------------------------------\n')
    print('---------- Perdedores -----------------')
    print('\n---------------------------------------\n')
    print(html_lista_perdedor)

    print('\n---------------------------------------\n')
    print('------- Comportamento Vencedor --------')
    print('\n---------------------------------------\n')
    print(html_lista_comportamento_vencedor)

    print('\n---------------------------------------\n')
    print('--- Quantidade de Partidas Time Out ------')
    print('\n---------------------------------------\n')
    print(html_lista_time_out)

    # restorno de valores para renderizacao em front-end
    return [dict(html_lista_hora),\
            dict(html_lista_vencedor),\
            dict(html_lista_perdedor),\
            dict(html_lista_comportamento_vencedor),\
            html_lista_time_out]