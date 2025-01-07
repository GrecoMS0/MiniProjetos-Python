import random

def dado_viciado():
    probabilidades = {
        1: 0.1,
        2: 0.2,
        3: 0.3,
        4: 0.4,
        5: 0.5,
        6: 0.6,
    }
    
    faces = list(probabilidades.keys())
    pesos = list(probabilidades.values())
    
    resultado = random.choices(faces, weights=pesos, k=1)[0]
    print(f"O dado viciado rolou: {resultado}")
    
def run():
    while True:
        dado_viciado()
        escolha = input("Deseja lançar o dado novamente? (S para Sim/0 para sair)").strip().upper()
        if escolha == "0":
            print("Saindo...")
            break
        elif escolha != "S":
            print("Opção inválida! Saindo...")
            break