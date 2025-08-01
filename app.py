from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index ():
    noticias = [
        {"titulo": "Notícia 1", "descricao": "Resumo sobre tecnologia", "imagem": "noticia1.jpg", "link": "https://exemplo.com/noticia1"},
        {"titulo": "Notícia 2", "descricao": "Resumo sobre educação", "imagem": "noticia2.jpg", "link": "https://exemplo.com/noticia2"},
        {"titulo": "Notícia 3", "descricao": "Resumo sobre meio ambiente", "imagem": "noticia3.jpg", "link": "https://exemplo.com/noticia3"},
        {"titulo": "Notícia 4", "descricao": "Resumo sobre ciência", "imagem": "noticia4.jpg", "link": "https://exemplo.com/noticia4"},
        {"titulo": "Notícia 5", "descricao": "Resumo sobre esportes", "imagem": "noticia5.jpg", "link": "https://exemplo.com/noticia5"},
        {"titulo": "Notícia 6", "descricao": "Resumo sobre cultura", "imagem": "noticia6.jpg", "link": "https://exemplo.com/noticia6"}
    ]
    return render_template("index.html", noticias=noticias)

@app.route('/professor')
def professor ():
    return render_template('professores.html')