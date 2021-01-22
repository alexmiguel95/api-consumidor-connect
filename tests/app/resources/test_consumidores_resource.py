import requests
import pytest

base_url = 'http://localhost:5000'

@pytest.fixture
def post_data_table_consumidores():
        body = {'nome': 'Test Tester',
                'email': 'test@test.com.br',
                'telefone': '41981234567',
                'senha': 'testando'}

        return requests.post(f'{base_url}/consumidores',json=body).json()

def test_post_data_table_consumidores(post_data_table_consumidores):

        result = str(post_data_table_consumidores)

        expected = "{'status': 'Created'}"

        assert result == expected


@pytest.fixture
def post_login_consumidores():

        body = {'email': 'test@test.com.br',
                'senha': 'testando'}

        return requests.post(f'{base_url}/login-consumidores',json=body).json()

def test_login_consumidores(post_login_consumidores):

        print(post_login_consumidores)

        access_token = post_login_consumidores['data']['access_token']

        print(access_token)


        expected = {
                        "data": {
                        "nome": "Test Tester",
                        "email": "test@test.com.br",
                        "telefone": "41981234567",
                        "access_token": access_token
                        }
                }


        assert post_login_consumidores == expected

@pytest.fixture
def get_data_table_consumidores():

        data = requests.get(f'{base_url}/consumidores').json()

        data = data['data']

        for item in data:
                if item["consumidores_produtores"] == [] and item['nome'] == 'Test Tester' and item['email'] == 'test@test.com.br':
                        return requests.get(f"{base_url}/consumidores/{item['id']}").json()['data']


def test_get_data_table_consumidores(get_data_table_consumidores):


        line_id = get_data_table_consumidores['id']

        result = get_data_table_consumidores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Test Tester', 'consumidores_produtores': []}

        assert result == expected

@pytest.fixture
def put_data_table_consumidores():

        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        access_token = requests.post(f'{base_url}/login-consumidores',json=body).json()['data']['access_token']

        data = requests.get(f'{base_url}/consumidores').json()['data']
        print(data,'sssssssssssssssssssssssssssssssss')

        for item in data:
                if item['nome'] == 'Test Tester' and item['email'] == 'test@test.com.br':

                        body = {'email': 'test@test.com.br',
                        'senha': 'testando'}

                        secret = requests.post(f'{base_url}/login-consumidores',json=body).json()['data']['access_token']

                        body = {"nome": 'Testado'}

                        requests.put(f"{base_url}/consumidores", headers={'Authorization': f'Bearer {secret}'}, json=body)
                        
                        return requests.get(f"{base_url}/consumidores/{item['id']}").json()['data']


def test_put_data_table_consumidores(put_data_table_consumidores):

        line_id = put_data_table_consumidores['id']

        result = put_data_table_consumidores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Testado', 'consumidores_produtores': []}

        assert result == expected

@pytest.fixture
def delete_data_table_consumidores():

        body = {'email': 'test@test.com.br',
        'senha': 'testando'}

        secret = requests.post(f'{base_url}/login-consumidores',json=body).json()['data']

        secret = secret['access_token']


        result = requests.delete(f"{base_url}/consumidores", headers={'Authorization': f'Bearer {secret}'})

        return result

def test_delete_data_table_consumidores(delete_data_table_consumidores):
        
        result = delete_data_table_consumidores.json()


        expected = {"status": "Ok"}

        assert result == expected