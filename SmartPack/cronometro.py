import time
import threading
import msvcrt  # Para capturar teclas no Windows

cancelar = False

def verificar_cancelamento():
    global cancelar
    while True:
        if msvcrt.kbhit():  # Verifica se alguma tecla foi pressionada
            tecla = msvcrt.getch().decode('utf-8').upper()
            if tecla == 'C':
                cancelar = True
                break

def cronometro():
    global cancelar
    cancelar = False

    try:
        print("Tempo a ser cronometrado.")
        horas = int(input("Horas....: ").strip())
        minutos = int(input("Minutos..: ").strip())
        segundos = int(input("Segundos.: ").strip())
    
        tempo_total = horas * 3600 + minutos * 60 + segundos  # Conversão para segundos
    
        if tempo_total <= 0:
            print("Tempo deve ser maior que zero!")
            return
    
        print(f"\nIniciando cronômetro para {horas:02}:{minutos:02}:{segundos:02}...\n")
        print("Pressione 'C' para cancelar o cronômetro.")

        # Inicia a thread para capturar o cancelamento
        thread_cancelar = threading.Thread(target=verificar_cancelamento, daemon=True)
        thread_cancelar.start()

        for restante in range(tempo_total, -1, -1):
            if cancelar:
                tempo_decorrido = tempo_total - restante
                print("\nContagem interrompida!")
                print(f"Tempo decorrido: {tempo_decorrido // 3600:02}:{(tempo_decorrido % 3600) // 60:02}:{tempo_decorrido % 60:02}")
                print(f"Tempo restante : {restante // 3600:02}:{(restante % 3600) // 60:02}:{restante % 60:02}")
                return

            h, m, s = restante // 3600, (restante % 3600) // 60, restante % 60
            print(f"   {h:02}:{m:02}:{s:02}", end='\r')
            time.sleep(1)

        print("\nTempo Esgotado!")
    except ValueError:
        print("\nEntrada inválida! Digite apenas números inteiros.\n")

def run():
    while True:
        cronometro()
        escolha = input("Deseja cronometrar novamente? (S para sim / 0 para voltar ao menu principal): ").strip().upper()
        if escolha == "0":
            print("Voltando ao menu principal...")
            break
        elif escolha != "S":
            print("Opção inválida! Saindo...")
            break
