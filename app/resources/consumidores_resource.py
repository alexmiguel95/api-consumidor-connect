from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response
from flask import request
from app.models.model import Consumidores, ConsumidoresSchema, Produtores, db
from flask_jwt_extended import jwt_required, get_jwt_identity
# Gerar hash da senha
from werkzeug.security import generate_password_hash


class ConsumidoresResource(Resource):
    # CREATE
    def post(self):
        data = request.get_json()

        consumidor = Consumidores(
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"],
            senha=(generate_password_hash(data["senha"]))
        )

        try:
            db.session.add(consumidor)
            db.session.commit()
            return build_api_response(HTTPStatus.CREATED)
        except IntegrityError:
            return build_api_response(HTTPStatus.BAD_REQUEST)

    # READ
    def get(self, id=0):
        if id > 0:
            return {
                "data": ConsumidoresSchema().dump(Consumidores.query.get(id))
            }

        return {
            "data": ConsumidoresSchema(many=True).dump(
                Consumidores.query.all()
            )
        }

    # UPDATE
    @jwt_required
    def put(self):
        data = request.get_json()
        logged_user_id = get_jwt_identity()

        consumidor = Consumidores.query.get(logged_user_id)
        if not consumidor:
            return build_api_response(HTTPStatus.NOT_FOUND)

        consumidor.nome = (
            data["nome"] if data.get("nome") else consumidor.nome
        )
        consumidor.email = (
            data["email"] if data.get("email") else consumidor.email
        )
        consumidor.telefone = (
            data["telefone"] if data.get("telefone") else consumidor.telefone
        )
        consumidor.senha = (
            generate_password_hash(data["senha"]) if data.get("senha")
            else consumidor.senha
        )

        if(data.get("consumidores_produtores")):
            consumidores_produtores = Produtores.query.filter(
                Produtores.id.in_(data["consumidores_produtores"])
            ).all()
            if len(consumidores_produtores) > 0:
                for produtor in consumidores_produtores:
                    consumidor.consumidores_produtores.append(produtor)
            else:
                consumidor.consumidores_produtores = []

        try:
            db.session.commit()
            return {"data": ConsumidoresSchema().dump(consumidor)}
        except IntegrityError:
            return build_api_response(HTTPStatus.CONFLICT)

    # DELETE
    @jwt_required
    def delete(self):
        logged_user_id = get_jwt_identity()

        consumidor = Consumidores.query.get(logged_user_id)
        if not consumidor:
            return build_api_response(HTTPStatus.NOT_FOUND)

        try:
            db.session.delete(consumidor)
            db.session.commit()
            return {
                "data": ConsumidoresSchema().dump(consumidor),
                "message": "Consumidor deletado!"
            }
        except IntegrityError:
            return build_api_response(HTTPStatus.BAD_REQUEST)
