import random

def gerar_aposta(qtde_numeros, intervalo):
    return sorted(random.sample(range(1, intervalo + 1), qtde_numeros))

def exibir_aposta(aposta):
    print("Sua aposta: ", " - ".join(f"{num:02}" for num in aposta))

def sorteio_loteria(qtde_numeros, intervalo):
    return sorted(random.sample(range(1, intervalo + 1), qtde_numeros))

def conferir_acertos(aposta, sorteio):
    return len(set(aposta) & set(sorteio))

def run():
    opcoes = {
        "1": "Mega-Sena (6 números de 1 a 60)",
        "2": "Quina (5 números de 1 a 80)",
        "0": "Sair"
    }
    
    while True:
        print("\nBem vindo ao Simulador de Loteria!")
        for key, value in opcoes.items():
            print(f"{key}. {value}")
        
        escolha = input("Escolha o tipo de loteria: ").strip()
        
        if escolha == "1":
            qtde_numeros = 6
            intervalo = 60
        elif escolha == "2":
            qtde_numeros = 5
            intervalo = 80
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")
            continue
        
        
        try:
            qtde_apostas = int(input("Escolha a quantidade de apostas a serem feitas: "))
            if qtde_apostas <= 0:
                print("A quantidade de apostas deve ser maior que zero!")
                return
        except ValueError:
            print("Por favor, insira um número válido!")
            continue
        print("\nGerando sua aposta...")
        apostas = []
        for _ in range(qtde_apostas):
            aposta = gerar_aposta(qtde_numeros, intervalo)
            apostas.append(aposta)
            exibir_aposta(aposta)
        
        simula = input("\nDeseja que seja feita simulação de sorteio? (S para sim / N para não): ").strip().upper()
        
        if simula == "S":
            sorteio = sorteio_loteria(qtde_numeros, intervalo)
            nenhum_acerto = True
            print("Números sorteados (SIMULAÇÃO): ", " - ".join(f"{num:02}" for num in sorteio))
        
            quadras = 0
            quinas = 0
            senas = 0
        
            for i, aposta in enumerate(apostas, start=1):
                acertos = conferir_acertos(aposta, sorteio)
                
                if escolha == "1" and acertos >= 4:
                    print(f"Aposta {i}: Você acertou {acertos} número(s)!")
                    nenhum_acerto = False
                    if acertos == 4:
                        quadras += 1
                    elif acertos == 5:
                        quinas += 1
                    elif acertos == 6:
                        senas += 1
                
                elif escolha == "2" and acertos >= 3:
                    print(f"Aposta {i}: Você acertou {acertos} número(s)!")
                    nenhum_acerto = False
                    if acertos == 3:
                        quadras += 1
                    elif acertos == 4:
                        quinas += 1
                    elif acertos == 5:
                        senas += 1
            
            if nenhum_acerto:
                print("Nenhum Acerto!")
            else:
                total_acertos = quadras + quinas + senas
                print("\nResumo dos resultados:")
                print(f"Jogos com Quadra: {quadras}")
                print(f"Jogos com Quina: {quinas}")
                print(f"Jogos com Sena: {senas}")
                print(f"Total de acertos no geral: {total_acertos}")
                
        elif simula == "N":
            continue
        else:
            print("Opção inválida!")
            continue
            
        novamente = input("\nDeseja fazer outra simulação? (S para sim / 0 para sair): ").strip().upper()
        if novamente == "0":
            print("Saindo...")
            break