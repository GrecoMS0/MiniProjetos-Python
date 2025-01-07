import time

def run():
    # Pergunta inicial sobre continuar ou sair
    escolha_continuar = input("Deseja prosseguir com o cálculo? (S para sim / 0 para sair): ").strip().upper()

    while True:
        if escolha_continuar == "S":
            calcular_carbono()
            escolha_continuar = input("Deseja fazer outro cálculo? (S para sim / 0 para sair): ").strip().upper()
        elif escolha_continuar == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Saindo do programa...")
            break

def calcular_carbono():
    try:
        km_carro = float(input("Quantos KM você dirige de carro por semana? -> "))
        km_onibus = float(input("Quantos KM você anda de ônibus por semana? -> "))
        km_aviao = float(input("Quantas horas de vôo você faz no mês? -> "))
        kwh_mes = float(input("Qual é o consumo de eletricidade em sua casa (kWh por mês)? -> "))
        
        fator_carro = 0.2
        fator_onibus = 0.1
        fator_aviao = 0.09  # Por Minuto
        fator_kwh = 0.5
        
        carbono_carro = km_carro * fator_carro * 4  # Semanal para mensal
        carbono_onibus = km_onibus * fator_onibus * 4
        carbono_aviao = km_aviao * 60 * fator_aviao  # Horas -> Minutos
        carbono_energia = kwh_mes * fator_kwh
        
        total_carbono = carbono_carro + carbono_onibus + carbono_aviao + carbono_energia
        
        print("\nPegada de carbono estimada:")
        print(f" |-- Carro........: {carbono_carro:.2f} Kg CO2/Mês")
        print(f" |-- Ônibus.......: {carbono_onibus:.2f} Kg CO2/Mês")
        print(f" |-- Avião........: {carbono_aviao:.2f} Kg CO2/Mês")
        print(f" |-- Eletricidade.: {carbono_energia:.2f} Kg CO2/Mês")
        print(f" |-- **Total......: {total_carbono:.2f} Kg CO2/Mês**\n")
    
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")

if __name__ == "__main__":
    run()
