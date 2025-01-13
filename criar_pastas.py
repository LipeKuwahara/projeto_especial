import os
from openpyxl import Workbook

# Caminho base onde os projetos serão criados
base_dir = "output_dir"

# Verifica se o caminho base existe
if not os.path.exists(base_dir):
    print(f"O caminho base '{base_dir}' não existe. Criando-o agora...")
    os.makedirs(base_dir)

# Solicita as informações do projeto
iniciais = input("INSIRA A INICIAL DO SEU NOME E SOBRENOME: ").strip().upper()
numero = input("INSIRA O NÚMERO DO PROJETO: ").strip().upper()
nome_op = input("INSIRA A OP: ").strip().upper()
nome_ambiente = input("INSIRA O NOME DO AMBIENTE: ").strip().upper()
nome_cliente = input("INSIRA O NOME DO CLIENTE: ").strip().upper()
nome_vendedor = input("INSIRA O NOME DO VENDEDOR: ").strip().upper()

# Constrói o nome do projeto
projeto_nome = f"{iniciais} - {numero} - {nome_op} - {nome_ambiente} - {nome_cliente} - {nome_vendedor}"

# Define a estrutura de pastas
estrutura = [
    "O.P.",
    "PERFIS E ITENS",
    "USINAGENS E DETALHAMENTOS",
    "ARQUIVOS"
]

# Caminho completo do projeto
projeto_path = os.path.join(base_dir, projeto_nome)

try:
    # Cria a pasta principal do projeto
    os.makedirs(projeto_path, exist_ok=True)
    print(f"Projeto criado: {projeto_path}")

    # Cria as subpastas
    for pasta in estrutura:
        subpasta_path = os.path.join(projeto_path, pasta)
        os.makedirs(subpasta_path, exist_ok=True)
        print(f"Subpasta criada: {subpasta_path}")

        # Se for a pasta "ARQUIVOS", cria um arquivo Excel e um Bloco de Notas em branco
        if pasta == "ARQUIVOS":
            # Cria um arquivo Excel em branco
            arquivo_excel_path = os.path.join(subpasta_path, "arquivo_em_branco.xlsx")
            wb = Workbook()
            wb.save(arquivo_excel_path)
            print(f"Arquivo Excel criado em: {arquivo_excel_path}")

            # Cria um arquivo de texto em branco
            arquivo_txt_path = os.path.join(subpasta_path, "arquivo_em_branco.txt")
            with open(arquivo_txt_path, "w") as txt_file:
                txt_file.write("")  # Arquivo vazio
            print(f"Bloco de Notas criado em: {arquivo_txt_path}")

    print("\nEstrutura de pastas criada com sucesso!")
except Exception as e:
    print(f"Erro ao criar as pastas: {e}")
