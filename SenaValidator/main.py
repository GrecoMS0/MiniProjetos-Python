import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import requests

def ler_apostas(arquivo):
    """ Lê as apostas de dentro do arquivo """
    try:
        with open(arquivo, 'r') as file:
            apostas = [list(map(int, linha.strip().split()))
            for linha in file.readlines()]
        return apostas
    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo {arquivo} não encontrado!")
        return []


def validar_apostas(apostas):
    """ Valida as apostas: 6 números por aposta e números entre 1 e 60 """
    for aposta in apostas:
        if len(aposta) != 6:
            messagebox.showerror("Erro", "Cada aposta deve conter exatamente 6 números!")
            return False
        if any(num <= 0 or num > 60 for num in aposta):
            messagebox.showerror("Erro", "Cada número deve ser entre 1 e 60!")
            return False
    return True


def obter_resultado_megasena():
    """ Busca resultado último sorteio """
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        dados = response.json()

        if "listaDezenas" in dados:
            numeros_sorteados = list(map(int, dados["listaDezenas"]))
        else:
            messagebox.showerror("Erro", "Chave para os números sorteados não encontrada!")
            return []
        return numeros_sorteados
    except requests.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao consultar o resultado: {e}")
        return []


def verifica_acertos(apostas, numeros_sorteados):
    """ Verifica acertos """
    resultados = {"quadra": [], "quina": [], "sena": []}
    for idx, aposta in enumerate(apostas):
        acertos = len(set(aposta) & set(numeros_sorteados))
        if acertos == 4:
            resultados["quadra"].append((idx + 1, aposta))
        elif acertos == 5:
            resultados["quina"].append((idx + 1, aposta))
        elif acertos == 6:
            resultados["sena"].append((idx + 1, aposta))
    return resultados


def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo de apostas", filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, arquivo)

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def executar_validacao():
    arquivo = entry_arquivo.get()
    apostas = []

    if arquivo and campo_apostas.get("1.0", tk.END).strip():
        resposta = messagebox.askyesno("Aviso", "Você forneceu tanto um arquivo quanto apostas manuais. Deseja usar o arquivo?")
        if resposta:
            apostas = ler_apostas(arquivo)
            if not apostas:
                messagebox.showerror("Erro", f"O arquivo {arquivo} enviado está vazio!")
                return
        else:
            apostas_texto = campo_apostas.get(
                "1.0", tk.END).strip().splitlines()
            apostas = [list(map(int, aposta.split()))
                       for aposta in apostas_texto]
    elif arquivo:
        apostas = ler_apostas(arquivo)
        if not apostas:
            messagebox.showerror("Erro", f"O arquivo {arquivo} enviado está vazio!")
            return
    elif campo_apostas.get("1.0", tk.END).strip():
        apostas_texto = campo_apostas.get("1.0", tk.END).strip().splitlines()
        apostas = [list(map(int, aposta.split())) for aposta in apostas_texto]
    else:
        messagebox.showerror("Erro", "Selecione um arquivo ou insira apostas manualmente!")
        return

    if not validar_apostas(apostas):
        return

    numeros_sorteados = obter_resultado_megasena()
    if not numeros_sorteados:
        return

    numeros_formatados = ' '.join(map(str, numeros_sorteados))
    resultados = verifica_acertos(apostas, numeros_sorteados)

    resultado_texto.config(state=tk.NORMAL)
    resultado_texto.delete("1.0", tk.END)

    resultado_texto.insert(tk.END, "-" * 29 + "\n")
    resultado_texto.insert(tk.END, f"|{'NÚMEROS SORTEADOS':^27}|\n")
    resultado_texto.insert(tk.END, "-" * 29 + "\n")
    resultado_texto.insert(tk.END, f"|{numeros_formatados:^27}|\n")
    resultado_texto.insert(tk.END, "-" * 29 + "\n\n")
    resultado_texto.insert(tk.END, "-" * 29 + "\n")
    if any(resultados.values()):
        resultado_texto.insert(tk.END, f"|{'SEUS ACERTOS':^27}|\n")
    else:
        resultado_texto.insert(tk.END, f"|{'NENHUM ACERTO!':^27}|\n")
    resultado_texto.insert(tk.END, "-" * 29 + "\n")

    for categoria, jogos in resultados.items():
        if jogos:
            resultado_texto.insert(tk.END, f"\n     {categoria.upper()} - {len(jogos)} jogo(s)      \n")
            resultado_texto.insert(tk.END, "-" * 29 + "\n")
            for idx, jogo in jogos:
                jogo_formatado = ' '.join(map(str, jogo))
                resultado_texto.insert(tk.END, f"| Jogo {idx:03}: {jogo_formatado} |\n")
            resultado_texto.insert(tk.END, "-" * 29 + "\n")

    resultado_texto.config(state=tk.DISABLED)
    

def mostrar_ajuda():
    """ Exibe janela de ajuda com instruções """

    ajuda = tk.Toplevel()
    ajuda.title("Ajuda")
    ajuda.resizable(False, False)
    ajuda.geometry("800x400")

    largura = 800
    altura = 400
    largura_tela = ajuda.winfo_screenwidth()
    altura_tela = ajuda.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    ajuda.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    texto_ajuda = """Instruções de uso:

    1. **Arquivo de Apostas (.txt)**:
        - O arquivo deve conter uma aposta por linha.
        - Cada aposta deve ter 6 números inteiros separados por espaço, como por exemplo:
          10 20 30 40 50 60
          5 15 25 35 45 55

    2. **Inserir Apostas Manualmente**:
        - Você também pode digitar ou colar suas apostas diretamente na caixa de texto abaixo.
        - Cada aposta deve estar em uma linha separada, com 6 números inteiros separados por espaço, como mostrado acima.

    3. **Validar**:
        - Clique em "Validar" após selecionar o arquivo ou inserir as apostas manualmente para ver os resultados de acertos.

    Espero que estas instruções ajudem!"""

    label_ajuda = tk.Label(ajuda, text=texto_ajuda, justify=tk.LEFT, font=(
        "Helvetica", 10), padx=10, pady=10)
    label_ajuda.pack(fill=tk.BOTH, expand=True)


def validar_input_aposta(texto):
    """ Permitir apenas números e espaços """
    return texto.isdigit() or texto == "" or texto.isspace()


# Criando a janela
janela = tk.Tk()
janela.title("Validador Mega-Sena")
janela.geometry("500x600")
janela.resizable(False, False)
janela.config(bg="#3d85c6")

# Título
label_titulo = tk.Label(janela, text="Validador de Apostas Mega-Sena", font=("Helvetica", 16, "bold"), bg="#3d85c6", fg="#ffffff")
label_titulo.pack(pady=20)

# Campo de seleção do arquivo
frame_arquivo = tk.Frame(janela, bg="#3d85c6")
frame_arquivo.pack(pady=10)

entry_arquivo = tk.Entry(frame_arquivo, font=("Helvetica", 12), width=30)
entry_arquivo.pack(side="left", padx=5, pady=5)

botao_buscar = tk.Button(frame_arquivo, text="Buscar", command=selecionar_arquivo, font=("Helvetica", 12), bg="#B0B0B0", fg="black", relief="flat", padx=10, pady=5, bd=2, highlightbackground="#3d85c6", highlightthickness=2)
botao_buscar.pack(side="left", padx=5, pady=5)

# Campo para inserir apostas manualmente
label_apostas = tk.Label(janela, text="Ou insira suas apostas manualmente:", font=("Helvetica", 12), bg="#3d85c6", fg="#ffffff")
label_apostas.pack(pady=10)

campo_apostas = ScrolledText(janela, wrap=tk.WORD, font=("Courier", 10), height=5, width=50, bg="#f9f9f9", fg="#333", bd=2, relief="sunken")
campo_apostas.pack(pady=10)

validar_aposta = janela.register(validar_input_aposta)

# Botão "Validar"
botao_validar = tk.Button(janela, text="Validar", command=executar_validacao, font=("Helvetica", 12), bg="#4CAF50", fg="black", relief="flat", padx=10, pady=5, bd=2, highlightbackground="#3d85c6", highlightthickness=2)
botao_validar.pack(pady=20)

# Botão de ajuda
botao_ajuda = tk.Button(janela, text="Ajuda", command=mostrar_ajuda, font=("Helvetica", 12), bg="#f39c12", fg="black", relief="flat", padx=10, pady=5, bd=2, highlightbackground="#3d85c6", highlightthickness=2)
botao_ajuda.pack(pady=10)

# Caixa de texto do resultado
resultado_texto = ScrolledText(janela, wrap=tk.WORD, font=("Courier", 10), height=10, width=55, bg="#f9f9f9", fg="#333", bd=2, relief="sunken")
resultado_texto.config(state=tk.DISABLED)
resultado_texto.pack(pady=10)

# Rodapé
rodape = tk.Label(janela, text="© 2024 Validador Mega-Sena", font=("Helvetica", 8), bg="#3d85c6", fg="#888")
rodape.pack(side="bottom", pady=10)

centralizar_janela(janela)
janela.mainloop()
