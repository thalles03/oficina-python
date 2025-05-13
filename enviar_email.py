import smtplib
from email.message import EmailMessage

# Caminho do relatório
arquivo_relatorio = 'relatorio.txt'

# Lê o conteúdo do relatório
with open(arquivo_relatorio, 'r', encoding='utf-8') as file:
    conteudo = file.read()

# Cria a mensagem de e-mail
mensagem = EmailMessage()
mensagem['Subject'] = '📊 Relatório de Livros Automatizado'
mensagem['From'] = 'relatorio@automacao.com'
mensagem['To'] = 'destinatario@exemplo.com'
mensagem.set_content(conteudo)

# Envia pelo servidor SMTP local (smtp4dev)
try:
    with smtplib.SMTP('localhost', 25) as smtp:  # Altere a porta se necessário
        smtp.send_message(mensagem)
        print("✅ E-mail enviado com sucesso (simulado pelo smtp4dev).")
except ConnectionRefusedError:
    print("❌ Erro: Não foi possível conectar ao servidor SMTP local. Verifique se o smtp4dev está em execução.")