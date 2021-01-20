import requests
import pytest

@pytest.fixture
def post_data_table_consumidores():
        body = {'nome': 'Test Tester',
                'email': 'test@test.com.br',
                'telefone': '41981234567'}

        return requests.post('http://localhost:5000/consumidores',json=body).json()

def test_post_data_table_consumidores(post_data_table_consumidores):

        result = str(post_data_table_consumidores)

        expected = "{'status': 'Created'}"

        assert result == expected

@pytest.fixture
def get_data_table_consumidores():

        data = requests.get('http://localhost:5000/consumidores').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567' and line['consumidores_produtores'] == []:
                        return requests.get(f"http://localhost:5000/consumidores/{line['id']}").json()['data']


def test_get_data_table_consumidores(get_data_table_consumidores):


        line_id = get_data_table_consumidores['id']

        result = get_data_table_consumidores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Test Tester', 'telefone': '41981234567', 'consumidores_produtores': []}

        assert result == expected

@pytest.fixture
def put_data_table_consumidores():

        body = {'nome': 'Testado'}

        data = requests.get('http://localhost:5000/consumidores').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':
                        requests.put(f"http://localhost:5000/consumidores/{line['id']}",json=body)
                        return requests.get(f"http://localhost:5000/consumidores/{line['id']}").json()['data']


def test_put_data_table_consumidores(put_data_table_consumidores):

        line_id = put_data_table_consumidores['id']

        result = put_data_table_consumidores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Testado', 'telefone': '41981234567', 'consumidores_produtores': []}

        assert result == expected

@pytest.fixture
def delete_data_table_consumidores():

        data = requests.get('http://localhost:5000/consumidores').json()

        data = data['data']

        result = 'deleted'

        for line in data:
                
                if line['nome'] == 'Testado' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':

                        requests.delete(f"http://localhost:5000/consumidores/{line['id']}")

                        data = requests.get('http://localhost:5000/consumidores').json()

                        data = data['data']

                        for line in data:

                                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                                        line['telefone'] == '41981234567':
                                        result = 'not deleted'

                return result

def test_delete_data_table_consumidores(delete_data_table_consumidores):
        
        result = delete_data_table_consumidores

        expected = 'deleted'

        assert result == expected