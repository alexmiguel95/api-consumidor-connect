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
###  Rotas públicas
####  POST /produtores
> Registra um novo Produtor. Todos os campos são obrigatórios.

Body:
```json
{
	"nome": "Alex Miguel",
	"email": "alexmiguel95@gmail.com",
	"telefone": "41998769061",
	"senha": "abc123!"
}
```
Response:
```json
{
	"status": "Created"
}
```

####  POST /login-produtores
> Logar como um Produtor.

Body:
```json
{
	"email": "alexmiguel95@gmail.com",
	"senha": "abc123!"
}
```
Response:
```json
{
  "data": {
    "nome": "Alex Miguel",
    "email": "alexmiguel95@gmail.com",
    "telefone": "4199869061",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTExNzkwMDcsIm5iZiI6MTYxMTE3OTAwNywianRpIjoiMGQ2YTRjNzgtZGM2ZS00MjY5LTk0NjktMWRlN2NjZTlkOGU4IiwiZXhwIjoxNjExNzgzODA3LCJpZGVudGl0eSI6MTMsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsInVzZXJfY2xhaW1zIjp7ImVtYWlsIjoiYWxleG1pZ3VlbDk1QGdtYWlsLmNvbSJ9fQ.bvASOXWme4O-XAe1Gnh3Vf2Hcg0kUnhO9KR_SmnvwXI"
  }
}
```

####  GET /produtores
> Recuperar todos os Produtores cadastrados.

Response:
```json
{
  "data": [
    {
      "produtores_produtos": [],
      "email": "denis@gmail.com",
      "id": 5,
      "telefone": "4165564",
      "nome": "Denis"
    },
    {
      "produtores_produtos": [
        {
          "descricao": "Muito boa",
          "link_video": "url_video",
          "id": 12,
          "link_foto": "{url_foto_1,url_foto2,url_foto3}",
          "nome": "Maça"
        }
      ],
      "email": "alex@gmail.com",
      "id": 8,
      "telefone": "4165564",
      "nome": "Alex"
    },
    {
      "produtores_produtos": [],
      "email": "paulo@gmail.com",
      "id": 12,
      "telefone": "4165564",
      "nome": "Paulo Santos"
    },
    {
      "produtores_produtos": [],
      "email": "alexmiguel95@gmail.com",
      "id": 13,
      "telefone": "4199869061",
      "nome": "Alex Miguel"
    }
  ]
}
```

####  GET /produtores/<int:id>
> Recuperar um Produtor específico.

Response:
```json
{
  "data": {
    "produtores_produtos": [],
    "email": "alexmiguel95@gmail.com",
    "id": 13,
    "telefone": "4199869061",
    "nome": "Alex Miguel"
  }
}
```

####  POST /consumidores
> Registra um novo Consumidor. Todos os campos são obrigatórios.

Body:
```json
{
	"nome": "Denis Rafael",
	"email": "denis.rafael@gmail.com",
	"telefone": "41998876656",
	"senha": "abc123!"
}
```
Response:
```json
{
	"status": "Created"
}
```

####  POST /login-consumidores
> Logar como um Consumidor.

Body:
```json
{
	"email": "denis.rafael@gmail.com",
	"senha": "abc123!"
}
```
Response:
```json
{
  "data": {
    "nome": "Denis Rafael",
    "email": "denis.rafael@gmail.com",
    "telefone": "41998876656",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTExNzk3MDQsIm5iZiI6MTYxMTE3OTcwNCwianRpIjoiN2EzYTYxNGMtZTJkZS00OTkxLWE2ZDYtMmY0YjIxZjMyOGU5IiwiZXhwIjoxNjExNzg0NTA0LCJpZGVudGl0eSI6NiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.zyCmapxypgsjn1xyKUYiHmeYioEO6GY0P3DXKtyWSE4"
  }
}
```

####  GET /consumidores
> Recuperar todos os Consumidores cadastrados.

Response:
```json
{
  "data": [
    {
      "consumidores_produtores": [],
      "email": "paulo@gmail.com",
      "id": 4,
      "nome": "Paulo Santos"
    },
    {
      "consumidores_produtores": [],
      "email": "denis.rafael@gmail.com",
      "id": 6,
      "nome": "Denis Rafael"
    }
  ]
}
```

####  GET /consumidores/<int:id>
> Recuperar um Consumidor específico.

Response:
```json
{
  "data": {
    "consumidores_produtores": [],
    "email": "denis.rafael@gmail.com",
    "id": 6,
    "nome": "Denis Rafael"
  }
}
```

###  Rotas privadas
Os endpoints a seguir estão disponíveis apenas para usuários com um token de autenticação. No header, é necessário adicionar o **Bearer** com o _access_token_ gerado na autenticação do usuário.
####  PUT /produtores
> Atualizar um Produtor.

Header:

Authorization: Bearer <_token_>

Body:
```json
{
	"email": "alexmiguel@gmail.com"
}
```
Response:
```json
{
  "data": {
    "produtores_produtos": [],
    "email": "alexmiguel@gmail.com",
    "id": 13,
    "telefone": "4199869061",
    "nome": "Alex Miguel"
  }
}
```

####  DELETE /produtores
> Apagar um Produtor e todos os Produtos dele.

Header:

Authorization: Bearer <_token_>

Response:
```json
{
  "status": "Ok"
}
```

####  PUT /consumidores
> Atualizar um Consumidor. Além de poder atualizar todos os campos informados no registro, é nessa rota onde podemos fazer o vínculo entre um Consumidor e vários Produtores, assim o Consumidor consegue ver os Produtos de Produtores específicos.

Header:

Authorization: Bearer <_token_>

Body:
```json
{
	"consumidores_produtores": [12, 8]
}
```
Response:
```json
{
  "data": {
    "consumidores_produtores": [
      {
        "produtores_produtos": [
          {
            "descricao": "Muito boa",
            "link_video": "url_video",
            "id": 12,
            "link_foto": "{url_foto_1,url_foto2,url_foto3}",
            "nome": "Maça"
          }
        ],
        "email": "alex@gmail.com",
        "id": 8,
        "telefone": "4165564",
        "nome": "Alex"
      },
      {
        "produtores_produtos": [],
        "email": "paulo@gmail.com",
        "id": 12,
        "telefone": "4165564",
        "nome": "Paulo Santos"
      }
    ],
    "email": "denis.rafael@gmail.com",
    "id": 6,
    "telefone": "41998876656",
    "nome": "Denis Rafael"
  }
}
```

####  DELETE /consumidores
> Apagar um Consumidor.
Header:

Authorization: Bearer <_token_>

Response:
```json
{
  "status": "Ok"
}
```

####  POST /produtos
> Cadastrar um Produto. O campo nome é obrigatório. Somente um Produtor consegue cadastrar um Produto.

Header:

Authorization: Bearer <_token_>

Body:
```json
{
	"nome": "Coco gelado",
	"descricao": "Muito doce",
	"link_foto": [
		"https://razoesparaacreditar.com/wp-content/uploads/2018/09/coco-verde-300x171.jpg",  "https://www.fapema.br/wp-content/uploads/2015/05/0coco.jpg"
	],
	"link_video": "https://www.youtube.com/watch?v=d1yDT2lbbTs&ab_channel=MalacachetaSEMFRONTEIRAS"
}
```

Response:
```json
{
  "status": "Created"
}
```

####  GET /produtos
> Recuperar todos os Produtos do Produtor. Ele recupera pelo token passado no Authorization.

Header:

Authorization: Bearer <_token_>
Response:
```json
{
  "data": [
    {
      "link_video": "https://www.youtube.com/watch?v=d1yDT2lbbTs&ab_channel=MalacachetaSEMFRONTEIRAS",
      "descricao": "Muito doce",
      "id": 14,
      "link_foto": "{https://razoesparaacreditar.com/wp-content/uploads/2018/09/coco-verde-300x171.jpg,https://www.fapema.br/wp-content/uploads/2015/05/0coco.jpg}",
      "nome": "Coco gelado"
    }
  ]
}
```

####  DELETE /produtos/<int:id_produto>
> Apagar um Produto. Só um Produtor pode apagar um produto.

Header:

Authorization: Bearer <_token_>

Response:
```json
{
  "status": "Ok"
}
```

&nbsp;  
#### Desenvolvedores
**[Denis Rafael](https://www.linkedin.com/)**, **[Alex Miguel](https://www.linkedin.com/in/alexmiguel95/)**, **[Nicolas da Silva](https://www.linkedin.com/in/nicolasknzmd/)**, **[Paulo Santos](https://www.linkedin.com/)**