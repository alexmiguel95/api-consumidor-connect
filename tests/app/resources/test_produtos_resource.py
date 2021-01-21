import requests
import pytest

base_url = 'http://localhost:5000'

@pytest.fixture
def post_data_table_produtos():

        body = {'nome': 'Test Tester',
        'email': 'test@test.com.br',
        'telefone': '41981234567',
        'senha': 'testando'}

        requests.post(f'{base_url}/produtores',json=body).json()

        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        secret = requests.post(f'{base_url}/login-produtores',json=body).json()['data']['access_token']

        body = {
	"nome": "Coco gelado",
	"descricao": "Muito doce",
	"link_foto": [
		"https://razoesparaacreditar.com/wp-content/uploads/2018/09/coco-verde-300x171.jpg",  "https://www.fapema.br/wp-content/uploads/2015/05/0coco.jpg"
	],
	"link_video": "https://www.youtube.com/watch?v=d1yDT2lbbTs&ab_channel=MalacachetaSEMFRONTEIRAS"
        }

        return requests.post(f'{base_url}/produtos', headers={'Authorization': f'Bearer {secret}'}, json=body).json()


def test_post_data_table_produtos(post_data_table_produtos):

        result = str(post_data_table_produtos)

        expected = "{'status': 'Created'}"

        assert result == expected


@pytest.fixture
def get_data_table_produtos():


        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        secret = requests.post(f'{base_url}/login-produtores',json=body).json()['data']['access_token']

        return requests.get(f'{base_url}/produtos', headers={'Authorization': f'Bearer {secret}'}).json()


def test_get_data_table_produtos(get_data_table_produtos):

        line_id = get_data_table_produtos['data'][0]['id']


        result = get_data_table_produtos

        expected = {
                        "data": [
                          {
                            "link_video": "https://www.youtube.com/watch?v=d1yDT2lbbTs&ab_channel=MalacachetaSEMFRONTEIRAS",
                            "descricao": "Muito doce",
                            "id": line_id,
                            "link_foto": "{https://razoesparaacreditar.com/wp-content/uploads/2018/09/coco-verde-300x171.jpg,https://www.fapema.br/wp-content/uploads/2015/05/0coco.jpg}",
                            "nome": "Coco gelado"
                          }
                        ]
                }


        assert result == expected

@pytest.fixture
def delete_data_table_produtos():


        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        secret = requests.post(f'{base_url}/login-produtores',json=body).json()['data']['access_token']

        line_id = requests.get(f'{base_url}/produtos', headers={'Authorization': f'Bearer {secret}'}).json()['data'][0]['id']

        result = requests.delete(f'{base_url}/produtos/{line_id}', headers={'Authorization': f'Bearer {secret}'}).json()

        requests.delete(f"{base_url}/produtores", headers={'Authorization': f'Bearer {secret}'})

        return result


def test_delete_data_table_produtos(delete_data_table_produtos):


        result = delete_data_table_produtos

        expected = {"status": "Ok"}


        assert result == expected
    


# @pytest.fixture
# def delete_data_table_produtos():

#         data = requests.get('http://localhost:5000/produtos').json()

#         data = data['data']

#         for line in data:
#                 if line['nome'] == 'Testado' and line['descricao'] == 'produto testado' and \
#                         line['link_foto'] == 'www.testef.com.br' and line['link_video'] == 'www.testev.com.br':

#                         requests.delete(f"http://localhost:5000/produtos/{line['id']}").json()

                        
#                         data = requests.get('http://localhost:5000/produtores').json()

#                         data = data['data']

#                         for line in data:
                        
#                                 if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
#                                         line['telefone'] == '41981234567':

#                                         requests.delete(f"http://localhost:5000/produtores/{line['id']}")

#                                         return 'deleted'
                


# def test_delete_data_table_produtos(delete_data_table_produtos):

#     result = delete_data_table_produtos

#     expected = 'deleted'

#     assert result == expected

