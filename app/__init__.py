from flask import Flask
from app.models.model import db, mg, ma
from environs import Env
from flask_restful import Api
from flask_jwt_extended import JWTManager
from secrets import token_hex
from app.resources.produtos_resource import ProdutosResource
from app.resources.login_produtores_resource import LoginProdutoresResource
from app.resources.produtores_resource import ProdutoresResource
from app.resources.consumidores_resource import ConsumidoresResource
from app.resources.login_consumidores_resource import LoginConsumidoresResource


def create_app(config="development"):
   env = Env()
   env.read_env()

   app = Flask(__name__)
   api = Api()


   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
      'SQLALCHEMY_TRACK_MODIFICATIONS'
   )
   app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')
   app.config['JWT_SECRET_KEY'] = token_hex(16)

   db.init_app(app)
   mg.init_app(app, db)
   ma.init_app(app)
   JWTManager(app)

   api.add_resource(
      LoginProdutoresResource,
      "/login-produtores"
   )
   api.add_resource(
      ProdutoresResource,
      "/produtores",
      "/produtores/<int:id>"
   )
   api.add_resource(
      ProdutosResource,
      "/produtos",
      "/produtos/<int:id_produto>"
   )
   api.add_resource(
      LoginConsumidoresResource,
      "/login-consumidores"
   )
   api.add_resource(
      ConsumidoresResource,
      "/consumidores",
      "/consumidores/<int:id>"
   )

   api.init_app(app)
   return app
