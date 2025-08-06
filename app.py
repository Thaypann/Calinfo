from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.before_request
def criar_tabelas_se_nao_existirem():
    if not hasattr(app, 'tabelas_criadas'):
        db.create_all()
        app.tabelas_criadas = True


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        flash('Email ou senha incorretos', 'danger')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado.', 'warning')
            return redirect(url_for('cadastro'))
        novo_usuario = Usuario(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha)
        )
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu com sucesso.', 'info')
    return redirect(url_for('index'))

@app.route('/usuarios')
def lista_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)