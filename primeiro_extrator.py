# primeiro_extrator.py
print("Iniciando a análise documental automatizada...")

# Simplesmente lê o conteúdo de um arquivo de texto e imprime
def extrair_texto_simples(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        print(f"\n--- Conteúdo do arquivo '{caminho_arquivo}' ---")
        print(conteudo)
        print(f"--- Fim do conteúdo ---")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Crie um arquivo de exemplo para testar
nome_arquivo_exemplo = "documento_exemplo.txt"
conteudo_exemplo = """
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

Entre:
EMPRESA ABC LTDA, com CNPJ 12.345.678/0001-90, doravante CONTRATANTE,
e
João Silva, CPF 123.456.789-00, doravante CONTRATADO.

CLÁUSULA PRIMEIRA: Objeto do Contrato
O CONTRATADO prestará serviços de consultoria jurídica trabalhista para a CONTRATANTE.

CLÁUSULA SEGUNDA: Prazo
O prazo de duração do presente contrato será de 12 (doze) meses, iniciando em 01/01/2025 e terminando em 31/12/2025.

CLÁUSULA TERCEIRA: Remuneração
A CONTRATANTE pagará ao CONTRATADO o valor mensal de R\$ 5.000,00 (cinco mil reais) até o dia 5 de cada mês.

CLÁUSULA QUARTA: Rescisão
Este contrato poderá ser rescindido por qualquer das partes mediante aviso prévio de 30 (trinta) dias.
"""
with open(nome_arquivo_exemplo, 'w', encoding='utf-8') as f:
    f.write(conteudo_exemplo)
print(f"Arquivo '{nome_arquivo_exemplo}' criado para teste.")

# Executa a função para extrair o texto do arquivo de exemplo
extrair_texto_simples(nome_arquivo_exemplo)

print("\nAnálise documental automatizada concluída por este script simples.")
