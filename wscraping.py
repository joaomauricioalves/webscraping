import smtplib
import ssl
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def solicitaURL(url):
    #vamos criar uma variável responsável por armazenar requests da url
    # e depois criar um objeto beautifulSoup
    resultado = requests.get(url)
    resultado.encoding = resultado.apparent_encoding
    soup = BeautifulSoup(resultado.text, 'html.parser')
    return soup

# a partir daqui criar uma função para obter as informações iniciais da notícia.
def tituloSempreUpdate(soup):
    title = soup.title.get_text()
    return title


def pegarInfoSempreUpdate(soup):
    info = soup.find_all('h3', class_='entry-title')
    mensagem = []
    i = 1
    while i < 6:
        mensagem.append(info[i].get_text())
        i += 1

    delimiter = '. \r\n'
    mensagem = delimiter.join(mensagem)
    mensagem = mensagem.replace(". ", ". <br/>")
    return mensagem


def tituloItsFoss(soup):
    title = soup.title.get_text()
    return title


def pegarInfoItsFoss(soup):
    info = soup.find_all('h2', class_='entry-title')
    mensagem = []
    i = 1
    while i < 6:
        mensagem.append(info[i].get_text())
        i += 1

    delimiter = '. \r\n'
    mensagem = delimiter.join(mensagem)
    mensagem = mensagem.replace(". ", ". <br/>")
    return mensagem

def main():
    sempre_update = "https://sempreupdate.com.br/category/noticias/"
    itsfoss = "https://itsfoss.com/all-blog-posts/"
    remetente = 'email@emailvalidodoremetente.com.br'
    destinatarios = ['teste1@teste.com.br', 'teste2@teste2.com.br']

    tam = len(destinatarios)
    i = 0
    dest = []
    while i < tam:
        dest.append(destinatarios[i])
        i += 1


    delimiter = ', '
    #DEST é a lista destinatários em forma de string
    dest = delimiter.join(dest)
    

    #informações do servidor de e-mail do remetente
    #altere tomando cuidado com número de porta do Servidor SMTP, servidor de envio de e-mails
    porta = 587
    usuario = 'usuario'
    senha = 'senha'
    msg = MIMEMultipart('alternative')

    # Cria o corpo da mensagem em HTML   
    html = """\
    <html>
    <head></head>
    <body>        
        <h2>"""f'{tituloSempreUpdate(solicitaURL(sempre_update))}'"""</h2>
        <p>"""f'{pegarInfoSempreUpdate(solicitaURL(sempre_update))}'"""</p>
        <a href="""f'{sempre_update}'""">Mais sobre Sempre Update</a>
        <h2>"""f'{tituloItsFoss(solicitaURL(itsfoss))}'"""</h2>
        <p>"""f'{pegarInfoItsFoss(solicitaURL(itsfoss))}'"""</p>
        <a href="""f'{itsfoss}'""">Mais sobre It's Foss!</a>
    </body>
    </html>"""
    #O próximo passo é anexar as configurações do corpo do e-mail, se usarão um texto plano ou HTML que escolhemos HTML
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'As últimas notícias'
    msg['From'] = remetente
    msg['To'] = dest
    #Aqui é iniciado procedimentos de criação de objeto SSL para o uso na autenticação com o servidor de e-mail SMTP
    context = ssl.create_default_context()
    #Em seguida ele pede o endereço do servidor de e-mail SMTP.
    with smtplib.SMTP_SSL("mail.teste.com.br", porta, context=context) as server:
    #aqui temos um tratamento de erros, pensando no cenário do não envio de e-mails.
        try:
            server.login(usuario, senha)
            server.sendmail(remetente, destinatarios, msg.as_string())
            print('E-mail enviado com sucesso!')
        except Exception:
            print("OH não! Aconteceu algum problema!")

if __name__ == '__main__':
    main()
