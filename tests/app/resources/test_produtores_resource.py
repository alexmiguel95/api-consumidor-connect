import requests
from requests_jwt import JWTAuth
import pytest

base_url = 'http://localhost:5000'

@pytest.fixture
def post_data_table_produtores():
        body = {'nome': 'Test Tester',
                'email': 'test@test.com.br',
                'telefone': '41981234567',
                'senha': 'testando'}

        return requests.post(f'{base_url}/produtores',json=body).json()

def test_post_data_table_produtores(post_data_table_produtores):

        result = str(post_data_table_produtores)

        expected = "{'status': 'Created'}"

        assert result == expected


@pytest.fixture
def post_login_produtores():

        body = {'email': 'test@test.com.br',
                'senha': 'testando'}

        return requests.post(f'{base_url}/login-produtores',json=body).json()

def test_login_produtores(post_login_produtores):

        access_token = post_login_produtores['data']['access_token']

        expected = {
                        "data": {
                        "nome": "Test Tester",
                        "email": "test@test.com.br",
                        "telefone": "41981234567",
                        "access_token": access_token
                        }
                }


        assert post_login_produtores == expected



@pytest.fixture
def get_data_table_produtores():

        data = requests.get(f'{base_url}/produtores').json()

        data = data['data']


        for item in data:
                if item["produtores_produtos"] == [] and item['nome'] == 'Test Tester' and item['email'] == 'test@test.com.br' and \
                        item['telefone'] == '41981234567':
                        return requests.get(f"{base_url}/produtores/{item['id']}").json()['data']


def test_get_data_table_produtores(get_data_table_produtores):


        line_id = get_data_table_produtores['id']

        result = get_data_table_produtores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Test Tester', 'telefone': '41981234567', "produtores_produtos": []}

        assert result == expected

@pytest.fixture
def put_data_table_produtores():

        body = {'email': 'test@test.com.br',
                'senha': 'testando'}

        access_token = requests.post(f'{base_url}/login-produtores',json=body).json()['data']['access_token']

        data = requests.get(f'{base_url}/produtores').json()['data']

        for item in data:
                if item["produtores_produtos"] == [] and item['nome'] == 'Test Tester' and item['email'] == 'test@test.com.br' and \
                        item['telefone'] == '41981234567':
                        print('aaaaaaaaaaaaaaaaaaaaaaaa',access_token)

                        body = {'nome': 'Testado'}

                        auth = JWTAuth(access_token)

                        requests.put(f"{base_url}/produtores", auth=auth, json=body)
                        return requests.get(f"{base_url}/produtores/{item['id']}").json()['data']


def test_put_data_table_produtores(put_data_table_produtores):

        line_id = put_data_table_produtores['id']

        result = put_data_table_produtores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Testado', 'telefone': '41981234567', "produtores_produtos": []}


        assert result == expected

@pytest.fixture
def delete_data_table_produtores():

        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        access_token = requests.post(f'{base_url}/login-produtores',json=body).json()['data']['access_token']

        auth = JWTAuth(access_token)

        result = requests.delete(f"{base_url}/produtores", auth=auth)

        print(result)

        # result = 'deleted'

        # for line in data:
                
        #         if line['nome'] == 'Testado' and line['email'] == 'test@test.com.br' and \
        #                 line['telefone'] == '41981234567':

        #                 requests.delete(f"http://localhost:5000/produtores/{line['id']}")

        #                 data = requests.get('http://localhost:5000/produtores').json()

        #                 data = data['data']

        #                 for line in data:

        #                         if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
        #                                 line['telefone'] == '41981234567':
        #                                 result = 'not deleted'

        #         return result

def test_delete_data_table_produtores(delete_data_table_produtores):
        
        result = delete_data_table_produtores

        expected = 'deleted'

        assert result == expected