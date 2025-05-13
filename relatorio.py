import csv

livros = []
local_arquivo = 'relatorio.csv'

# Lê os dados do CSV
with open(local_arquivo, 'r', encoding='UTF-8') as arquivo_csv:
     leitor = csv.DictReader(arquivo_csv)
     for linha in leitor:
          preco = float(linha['preco'].replace('£', ''))
          livros.append({
                'preco': preco,
                'titulo': linha['titulo'],
                'link': linha['link']
          })

# Calcula as métricas
total_livros = len(livros)
valor_total = sum(livro['preco'] for livro in livros)
media_valor = valor_total / total_livros
livro_mais_caro = max(livros, key=lambda livro: livro['preco'])
livro_mais_barato = min(livros, key=lambda livro: livro['preco'])

# Escreve o relatório
with open('relatorio.txt', 'w', encoding='UTF-8') as relatorio:
     relatorio.write('--------- Relatório de Livros ---------\n')
     relatorio.write(f"Quantidade de livros: {total_livros}\n")
     relatorio.write(f"Livro mais caro: {livro_mais_caro['titulo']} (£{livro_mais_caro['preco']:.2f})\n")
     relatorio.write(f"Link: {livro_mais_caro['link']}\n")
     relatorio.write(f"Livro mais barato: {livro_mais_barato['titulo']} (£{livro_mais_barato['preco']:.2f})\n")
     relatorio.write(f"Link: {livro_mais_barato['link']}\n")
     relatorio.write(f"Valor total dos livros: £{valor_total:.2f}\n")
     relatorio.write(f"Média de preço: £{media_valor:.2f}\n")