import time

def run():
    while True:
        opcoes = {
            "1": ("Temperatura (Celsius <-> Fahrenheit)", converter_temperatura),
            "2": ("Distância (Quilômetros <-> Milhas)", converter_distancia),
            "3": ("Peso (Quilos <-> Libras)", converter_peso),
            "0": ("Sair", None),
        }
    
        print("=== Conversor de Unidades ===")
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave}. {descricao}")
    
        escolha = input("\nDigite o número da conversão desejada: ")
    
        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            if funcao:
                print(f"\nExecutando {descricao}...\n")
                funcao()
            else:
                print("Saindo...")
                time.sleep(0.5)
                break
        else:
            print("Opção inválida. Tente novamente!")
            time.sleep(1)

def converter_temperatura():
    while True:
        print("\n--- Conversão de Temperatura ---")
        tipo = input("Digite 'C' para converter °C -> °F ou 'F' para °F -> °C: ").strip().upper()
        if tipo == "C":
            try:
                celsius = float(input("Digite a temperatura em °C: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "F":
            try:
                fahrenheit = float(input("Digite a temperatura em °F: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")
        
        escolha = input("\nDeseja fazer outra conversão? (S para sim / 0 para voltar ao menu): ").strip().upper()
        if escolha == "0":
            break
        elif escolha != "S":
            print("Opção inválida! Voltando ao menu principal...")
            break
        
        time.sleep(1)

def converter_distancia():
    while True:
        print("\n--- Conversão de Distância ---")
        tipo = input("Digite 'K' para converter de KM -> MI ou 'M' para MI -> KM: ").strip().upper()
        if tipo == "K":
            try:
                km = float(input("Digite a distância em km: "))
                milhas = km * 0.621371
                print(f"{km} km equivale a {milhas:.2f} milhas")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "M":
            try:
                milhas = float(input("Digite a distância em milhas: "))
                km = milhas / 0.621371
                print(f"{milhas} milhas equivale a {km:.2f} km")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")
        
        escolha = input("\nDeseja fazer outra conversão? (S para sim / 0 para voltar ao menu): ").strip().upper()
        if escolha == "0":
            break
        elif escolha != "S":
            print("Opção inválida! Voltando ao menu principal...")
            break
        
        time.sleep(1)

def converter_peso():
    while True:
        print("\n--- Conversão de Peso ---")
        tipo = input("Digite 'K' para converter de KG -> LB ou 'L' para LB -> KG: ").strip().upper()
        if tipo == "K":
            try:
                quilos = float(input("Digite o peso em kg: "))
                libras = quilos * 2.20462
                print(f"{quilos} kg equivale a {libras:.2f} libras")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "L":
            try:
                libras = float(input("Digite o peso em libras: "))
                quilos = libras / 2.20462
                print(f"{libras} libras equivale a {quilos:.2f} kg")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        elif tipo == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")
        
        escolha = input("\nDeseja fazer outra conversão? (S para sim / 0 para voltar ao menu): ").strip().upper()
        if escolha == "0":
            break
        elif escolha != "S":
            print("Opção inválida! Voltando ao menu principal...")
            break
        
        time.sleep(1)

if __name__ == "__main__":
    run()
