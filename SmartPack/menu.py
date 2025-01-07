import time
import calculadora_carbono
import conversor_unidades

def menu():
    opcoes ={
        "1": ("Calculadora de Carbono", calculadora_carbono.run),
        "2": ("Conversor de Unidades", conversor_unidades.run),
        "0": ("Sair", None),
    }
    
    print("\nBem-Vindo ao MultiTool Python!")
    for chave, (descricao, _) in opcoes.items():
        print(f"{chave}. {descricao}")
    
    escolha = input("\nDigite sua escolha: ")
    
    if escolha in opcoes:
        descricao, funcao = opcoes[escolha]
        if funcao:
            print(f"\nExecutando: {descricao}...\n")
            time.sleep(0.5)
            funcao()
        else:
            print("Saindo...")
            time.sleep(0.5)
    else:
        print("Opção Inválida. Tente novamente!")
        time.sleep(0.5)
        menu()
        
if __name__ == "__main__":
    menu()