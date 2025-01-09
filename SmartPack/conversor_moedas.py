import requests
from math import ceil

def obter_taxas():
    try:
        url = "https://open.er-api.com/v6/latest"
        moeda_base = "BRL"
        response = requests.get(f"{url}/{moeda_base}")
        response.raise_for_status()
        dados = response.json()
        
        if dados["result"] == "success":
            return dados["rates"]
        else:
            print("Erro ao obter taxas de câmbio")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
        return None
    
def obter_nomes_moedas():
    try:
        url = "https://openexchangerates.org/api/currencies.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar API para nomes das moedas: {e}")
        return{}
'''
def exibir_tabela(moedas, nomes_moedas, colunas=4):
    print("\nTabela de Moedas Disponíveis:")
    linhas = ceil(len(moedas) / colunas)
    for linha in range(linhas):
        for coluna in range(colunas):
            indice = linha + coluna * linhas
            if indice < len(moedas):
                moeda = moedas[indice]
                nome = nomes_moedas.get(moeda, moeda)
                print(f"{indice + 1}. {nome} ({moeda})", end="\t")
        print()
'''

def exibir_tabela(moedas, nomes_moedas, colunas=3):
    print("\nTabela de Moedas Disponíveis:")
    
    # Definir largura fixa para as colunas
    largura_coluna = 40
    
    linhas = ceil(len(moedas) / colunas)
    
    for linha in range(linhas):
        for coluna in range(colunas):
            indice = linha + coluna * linhas
            if indice < len(moedas):
                moeda = moedas[indice]
                nome = nomes_moedas.get(moeda, moeda)
                
                # Alinhar o índice, moeda e nome
                print(f"{indice + 1:<5}.{moeda:<10}{nome.ljust(largura_coluna)}", end="  ")
        print()  # Nova linha depois de cada linha de moedas



def conversor_moedas():
    taxas = obter_taxas()
    if not taxas:
        print("Não foi possível obter as taxas. Tente novamente mais tarde.")
        return
    
    nomes_moedas = obter_nomes_moedas()
    moedas = list(taxas.keys())
    
    exibir_tabela(moedas, nomes_moedas)
    
    try:
        escolha_origem = int(input("\nEscolha o número da moeda origem: ")) - 1
        if escolha_origem not in range(len(moedas)):
            print("Moeda origem inválida!")
            return
        moeda_origem = moedas[escolha_origem]
    except ValueError:
        print("Entrada Inválida!")
        return
    
    exibir_tabela(moedas, nomes_moedas)
    
    try:
        escolha_destino = int(input("\nEscolha o número da moeda destino: ")) - 1
        if escolha_destino not in range(len(moedas)):
            print("Moeda destino inválida!")
            return
        moeda_destino = moedas[escolha_destino]
    except ValueError:
        print("Entrada Inválida!")
        return
    
    try:
        valor = float(input(f"Valor em {moeda_origem} a ser convertido para {moeda_destino}: "))
        taxa_origem_para_destino = taxas[moeda_destino] / taxas[moeda_origem]
        resultado = valor * taxa_origem_para_destino
        print("+" + "-"*35 + "+")
        print(f"| {valor:.2f} {moeda_origem} equivale a {resultado:.2f} {moeda_destino} |")
        print("+" + "-"*35 + "+")
        
        cotacao_origem_para_brl = taxas[moeda_origem]
        cotacao_destino_para_brl = taxas[moeda_destino]
        
        print(f"\nCotação {moeda_origem}..........: {cotacao_origem_para_brl:.2f} {moeda_origem} para 1 BRL")
        print(f"Cotação {moeda_destino}..........: {cotacao_destino_para_brl:.2f} {moeda_destino} para 1 BRL")
        print(f"Cotação {moeda_destino} para {moeda_origem}.: {1 / cotacao_destino_para_brl:.2f} {moeda_origem} para 1 {moeda_destino}")
        
    except ValueError:
        print("Entrada Inválida! Digit um valor numérico!")

def run():
    while True:
        conversor_moedas()
        escolha = input("Deseja fazer outra conversão? (S para sim / 0 para sair): ").strip().upper()
        if escolha == "0":
            print("Saindo...")
            break
        elif escolha != "S":
            print("Opção inválida! Saindo...")
            break