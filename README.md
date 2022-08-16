# webscraping

<p>O código que será explicado fará consultas em um sites específicos, em seguida realizará extração e tratamento para ao final ser enviado por e-mail as notícias no formato HTML.</p>

<p>No exemplo será extraído o conteúdo das páginas <a href="https://sempreupdate.com.br/category/noticias/">Sempre Update</a> e do <a =href="https://itsfoss.com/all-blog-posts/">It's Foss</a>, que tratam das notícias do mundo linux e open source. Essa técnica pode ser aplicada a outras páginas, mudando nomes de classes e tags HTML analisadas.</p>

<p>Na conclusão será salvo como uma aplicação que rodará em um server linux, sendo atrelado ao CRONTAB para fazer com que seja consultado de X em X tempo.</p>

<p>Para iniciar, usaremos um Server CENTOS, já previamente configurado. Ele já possui o Python instalado e será necessário definir o diretório onde será criado o arquivo.py, aplicar ao Virtualenv para a criação de um ambiente virtual para o desenvolvimento da ferramenta. Caso tenha o desejo de replicar a experiência no sistema operacional Windows, funcionará, claro que obdecendo aos a mesma lógica de diretório para o arquivo.py e execução do Virtualenv.</p>

<p>Após criar um ambiente virtual, que nesse exemplo chamamos de (web), vamos instalar algumas bibliotecas que serão necessárias como, requests, beautiful soup, ssl, pip install requests, pip install beautifulsoup4 e pip install ssl</p>
<p></p>
