from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index ():
    noticias = [
        {"titulo": "VII Secitex do IFRN aborda emergência climática com foco no “Sertão e mar”", "descricao": "23/07/2025 Blog de Assis", "imagem": "noticia1.png", "link": "https://blogdeassis.com.br/2025/vii-secitex-do-ifrn-aborda-emergencia-climatica-com-foco-no-sertao-e-mar/448088/"},
        {"titulo": "Parceria entre IFRN e Prefeitura de São Gonçalo garante formação digital para servidores municipais", "descricao": "23/07/2025 Prefeitura São Gonçalo do Amarante", "imagem": "noticia2.png", "link": "https://saogoncalo.rn.gov.br/parceria-entre-ifrn-e-prefeitura-de-sao-goncalo-garante-formacao-digital-para-servidores-municipais/"},
        {"titulo": "Gabarito IFRN 2025 para professores sai pela Funcern", "descricao": "21/07/2025 Ache concursos", "imagem": "noticia3.png", "link": "https://www.acheconcursos.com.br/noticias/gabarito-ifrn-2025-para-professores-sai-pela-funcern-82256"},
        {"titulo": "IFRN divulga gabarito do concurso realizado pela FUNCERN", "descricao": "20/07/2025 FII Brasil", "imagem": "noticia4.jpg", "link": "https://fiibrasil.com/concurso/ifrn-rn-gabarito-concurso-01-2025/"},
        {"titulo": "Confira vagas de empregos no Rio Grande do Norte", "descricao": "04/08/2025 - Por g1 RN", "imagem": "noticia5.png", "link": "https://g1.globo.com/rn/rio-grande-do-norte/noticia/2025/08/04/confira-vagas-de-emprego-no-rio-grande-do-norte.ghtml"},
        {"titulo": "'Com EAD, impossível ser boa profissional' x 'Sem EAD, eu não teria diploma': os dois lados da educação à distância, segundo alunos", "descricao": "03/08/2025 - Por Luiza Tenente, g1", "imagem": "noticia6.png", "link": "https://g1.globo.com/educacao/noticia/2025/08/03/com-ead-impossivel-ser-boa-profissional-x-sem-ead-eu-nao-teria-diploma-os-dois-lados-da-educacao-a-distancia-segundo-alunos.ghtml"}
    ]
    return render_template("index.html", noticias=noticias)

@app.route('/professor')
def professor ():
    return render_template('professores.html')