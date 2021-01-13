from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
mg = Migrate()


produtores_consumidores = db.Table(
    "produtores_consumidores",
    db.Column("produtores_id", db.Integer, db.ForeignKey("produtores.id")),
    db.Column("consumidores_id", db.Integer, db.ForeignKey("consumidores.id"))
)


class Produtores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String)
    telefone = db.Column(db.String)

    produtores_produtos = db.relationship(
        "Produtos",
        back_populates="produtos_produtores"
    )


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String)
    link_foto = db.Column(db.String)
    link_video = db.Column(db.String)

    fk_produtores = db.Column(db.Integer, db.ForeignKey("produtores.id"))
    produtos_produtores = db.relationship(
        "Produtores",
        back_populates="produtores_produtos"
    )


class Consumidores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String)
    telefone = db.Column(db.String)
