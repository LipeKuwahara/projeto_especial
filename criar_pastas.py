import os

# Caminho base onde os projetos serão criados
base_dir = "output_dir"

# Verifica se o caminho base existe
if not os.path.exists(base_dir):
    print(f"O caminho base '{base_dir}' não existe. Criando-o agora...")
    os.makedirs(base_dir)

# Solicita as informações do projeto
numero = input("INSIRA O NÚMERO DO PROJETO: ").strip().upper()
nome_op = input("INSIRA A OP: ").strip().upper()
nome_ambiente = input("INSIRA O NOME DO AMBIENTE: ").strip().upper()
nome_cliente = input("INSIRA O NOME DO CLIENTE: ").strip().upper()
nome_vendedor = input("INSIRA O NOME DO VENDEDOR: ").strip().upper()

# Constrói o nome do projeto
projeto_nome = f"FK - {numero} - {nome_op} - {nome_ambiente} - {nome_cliente} - {nome_vendedor}"

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

    print("\nEstrutura de pastas criada com sucesso!")
except Exception as e:
    print(f"Erro ao criar as pastas: {e}")
