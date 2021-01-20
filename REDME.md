# Consumidor-Connetc API

|   Descrição	|   Tecnologias 	|
|---	|---	|
|Os pequenos negócios e produtores locais são extremamente importantes para a economia. Infelizmente, a maioria acaba comprando de empresas tradicionais. |  Python com as bibliotecas: _Pytest_, _SQLAlchemy_, _Migrations_, _Marshmallow_, _Flask-RESTful_ e _Flask-JWT_	|
Nosso objetivo é incentivar e aproximar os pequenos negócios e produtores locais dos consumidores, através de um sistema simples onde os produtores podem divulgar seus produtos. Os consumidores se cadastram na plataforma e seguem os produtores, e assim se informam dos produtos| 

---
&nbsp; 
## Endpoints
###  Base URL: 
&nbsp; 
###  Rotas públicas:
####  POST /produtores
> Registra um novo Produtor. Todos os campos são obrigatórios.

```json
{
	"nome": "Alex Miguel",
	"email": "alexmiguel95@gmail.com",
	"telefone": "41998769061",
	"senha": "abc123!"
}
```
####  POST /login-produtores
> Logar como um Produtor.

```json
{
	"email": "alexmiguel95@gmail.com",
	"senha": "abc123!"
}
```
GET /produtores

GET /produtores/id

PUT /produtores/id

DELETE /produtores/id

###  POST /produtos
POST /produtos

GET /produtos

PUT /produtos/id

DELETE /produtos/id


&nbsp;

###  Consumidores
POST /consumidores

GET /consumidores

GET /consumidores/id

PUT /consumidores/id

DELETE /consumidores/id

&nbsp;  
#### Desenvolvedores
**[Denis Rafael](https://www.linkedin.com/in/alexmiguel95/)**, **[Alex Miguel](https://www.linkedin.com/in/alexmiguel95/)**, **[Nicolas da Silva](https://www.linkedin.com/in/nicolasknzmd/)**, **[Paulo Santos](https://www.linkedin.com/in/alexmiguel95/)**
