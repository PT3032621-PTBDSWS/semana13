from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import CadastroForm
from .models import db, Usuario
from .email import send_email
from config import Config
import os

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    form = CadastroForm()
    nome_usuario = "Desconhecido"

    if form.validate_on_submit():
        nome = form.nome.data.strip()
        email = form.email.data.strip()

        # Verifica se já existe usuário com mesmo e-mail (opcional)
        existente = Usuario.query.filter_by(email=email).first()
        if existente:
            flash("Já existe um usuário com esse e-mail.", "warning")
            nome_usuario = existente.nome
        else:
            novo = Usuario(nome=nome, email=email)
            db.session.add(novo)
            db.session.commit()

            # Envia e-mails
            admin_email = os.getenv("ADMIN_EMAIL", Config.ADMIN_EMAIL)
            corpo = (
                "Novo usuário cadastrado:\n"
                "Prontuário: PT3032621\n"
                "Nome: Gustavo Maximo da Silva\n"
                f"Usuário (email): {novo.email}"
            )
            # Tenta enviar para admin e para o próprio usuário
            send_email(admin_email, "Novo cadastro no sistema", corpo)
            send_email(novo.email, "Seu cadastro foi realizado", corpo)

            flash("Usuário cadastrado com sucesso!", "success")
            nome_usuario = novo.nome

            # redireciona para evitar reenvio no refresh
            return redirect(url_for("main.index"))

    usuarios = Usuario.query.order_by(Usuario.id.asc()).all()
    return render_template("index.html", form=form, usuarios=usuarios, nome=nome_usuario)
