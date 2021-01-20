from flask_restful import Resource
from flask import request
from app.services.http import build_api_response
from app.services.consumidores_service import get_consumidor
from http import HTTPStatus
# Para criar o token
from flask_jwt_extended import create_access_token
from datetime import timedelta
# Para verificar a senha que esta criptografada no BD
from werkzeug.security import check_password_hash


class LoginConsumidoresResource(Resource):
    def post(self):
        data = request.get_json()

        # Verificar se o email esta cadastrado.
        consumidor = get_consumidor(data["email"])
        if consumidor is None:
            return build_api_response(HTTPStatus.UNAUTHORIZED)

        # Verificar se a senha é a mesma que está criptografada no BD.
        # Passar a senha criptografada do BD, e a senha que veio pelo post
        check_password = check_password_hash(consumidor.senha, data["senha"])
        if check_password is False:
            return build_api_response(HTTPStatus.UNAUTHORIZED)

        # Gerar o token
        access_token = create_access_token(
            identity=consumidor.id, expires_delta=timedelta(days=7)
        )

        return {"data": {
            "nome": consumidor.nome,
            "email": consumidor.email,
            "telefone": consumidor.telefone,
            "access_token": access_token
        }}
