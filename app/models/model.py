from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import fields


db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


# Tabela auxilar N:N entre Produtores e Consumidores
tb_produtores_consumidores = db.Table(
    "tb_produtores_consumidores",
    db.Column("fk_produtores", db.Integer, db.ForeignKey("produtores.id")),
    db.Column("fk_consumidores", db.Integer, db.ForeignKey("consumidores.id"))
)


class Produtores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String)
    telefone = db.Column(db.String)

    # Relação 1:N entre Produtores e Produtos
    produtores_produtos = db.relationship(
        "Produtos",
        back_populates="produtos_produtores"
    )

    # Relação N:N  entre Produtores e Consumidores
    produtores_consumidores = db.relationship(
        "Consumidores",
        secondary=tb_produtores_consumidores,
        back_populates='consumidores_produtores'
    )


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String)
    link_foto = db.Column(db.String)
    link_video = db.Column(db.String)

    # Relação N:1 Entre Produtos e Produtores
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

    # Relação N:N  entre Consumidores e Produtores
    consumidores_produtores = db.relationship(
        "Produtores",
        secondary=tb_produtores_consumidores,
        back_populates="produtores_consumidores"
    )


# Schemas
class ProdutoresSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Produtores

    id = ma.auto_field()
    nome = ma.auto_field()
    email = ma.auto_field()
    telefone = ma.auto_field()


class ConsumidoresSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Consumidores

    id = ma.auto_field()
    nome = ma.auto_field()
    email = ma.auto_field()
    telefone = ma.auto_field()
    consumidores_produtores = fields.Nested(ProdutoresSchema, many=True)


class ProdutosSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Produtos

    id = ma.auto_field()
    nome = ma.auto_field()
    descricao = ma.auto_field()
    link_foto = ma.auto_field()
    link_video = ma.auto_field()
