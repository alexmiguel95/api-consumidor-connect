from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response
from flask import request
from app.models.model import Produtores, ProdutoresSchema, Produtos, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash


class ProdutoresResource(Resource):
    def post(self):
        data = request.get_json()

        produtor = Produtores(
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"],
            senha=(generate_password_hash(data["senha"]))
        )

        try:
            db.session.add(produtor)
            db.session.commit()
            return build_api_response(HTTPStatus.CREATED)
        except IntegrityError:
            return build_api_response(HTTPStatus.BAD_REQUEST)

    def get(self, id=0):
        if id > 0:
            return {"data": ProdutoresSchema().dump(Produtores.query.get(id))}

        return {
            "data": ProdutoresSchema(many=True).dump(Produtores.query.all())
        }

    @jwt_required
    def put(self):
        logged_user_id = get_jwt_identity()
        produtor = Produtores.query.get(logged_user_id)
        data = request.get_json()

        if not produtor:
            return build_api_response(HTTPStatus.NOT_FOUND)

        produtor.nome = (data["nome"] if data.get("nome") else produtor.nome)
        produtor.email = (
            data["email"] if data.get("email") else produtor.email
        )
        produtor.telefone = (
            data["telefone"] if data.get("telefone") else produtor.telefone
        )
        produtor.senha = (
            generate_password_hash(data["senha"]) if data.get("senha")
            else produtor.senha
        )

        try:
            db.session.commit()
            return {"data": ProdutoresSchema().dump(produtor)}
        except IntegrityError:
            return build_api_response(HTTPStatus.CONFLICT)

    @jwt_required
    def delete(self):
        logged_user_id = get_jwt_identity()
        produtor = Produtores.query.get(logged_user_id)
        if not produtor:
            return build_api_response(HTTPStatus.NOT_FOUND)

        # Deletar todos os produtos do produtor
        Produtos.query.filter_by(
            fk_produtor=logged_user_id
        ).delete()

        try:
            db.session.delete(produtor)
            db.session.commit()
            return {
                "data": ProdutoresSchema().dump(produtor),
                "message": "Produtor deletado!"
            }
        except IntegrityError:
            return build_api_response(HTTPStatus.BAD_REQUEST)
