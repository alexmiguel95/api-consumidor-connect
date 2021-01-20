from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response
from flask import request
from app.models.model import Produtos, ProdutosSchema, db, Produtores
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity


class ProdutosResource(Resource):
    @jwt_required
    def post(self):
        data = request.get_json()

        produto = Produtos(
            nome=data["nome"],
            descricao=data["descricao"],
            link_foto=data["link_foto"],
            link_video=data["link_video"],
            fk_produtores=data["fk_produtores"]
        )

        # Verificar se o ID e email do token é de um Produtor cadastrado
        produtor = Produtores.query.filter_by(
            id=produtor_token_id, email=produtor_token_email
        ).first()

        # Salvar o produto se encontrar o produtor que foi passado no token
        if produtor is not None:
            links_fotos = []

            produto = Produtos(
                nome=data["nome"],
                descricao=data["descricao"],
                link_foto=links_fotos,
                link_video=data["link_video"],
                fk_produtor=get_jwt_identity()
            )

            if(data.get("link_foto")):
                link_foto = data.get("link_foto")

                if len(link_foto) > 0:
                    for foto in link_foto:
                        produto.link_foto.append(foto)

            try:
                db.session.add(produto)
                db.session.commit()
                return build_api_response(HTTPStatus.CREATED)
            except IntegrityError:
                return build_api_response(HTTPStatus.BAD_REQUEST)

    def get(self, id=0):
        if id > 0:
            return {"data": ProdutosSchema().dump(Produtos.query.get(id))}

        return {
            "data": ProdutosSchema(many=True).dump(Produtos.query.filter_by(
                fk_produtor=produtor_token_id
            ))
        }

    @jwt_required
    def delete(self, id_produto: int):
        # Pegar ID e email do token
        produtor_token_id = get_jwt_identity()
        produtor_token_email = get_jwt_claims().get("email")

        # Verificar se o ID e email do tokené de um Produtor cadastrado
        produtor = Produtores.query.filter_by(
            id=produtor_token_id, email=produtor_token_email
        ).first()

        # Deletar o produto se encontrar o produtor que foi passado no token
        if produtor is not None:
            deletar_produto = Produtos.query.filter_by(
                id=id_produto,
                fk_produtor=produtor_token_id
            ).delete()
            if deletar_produto == 0:
                return build_api_response(HTTPStatus.NOT_FOUND)

            db.session.commit()
            return build_api_response(HTTPStatus.OK)
