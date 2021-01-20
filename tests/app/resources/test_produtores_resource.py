import requests
import pytest

@pytest.fixture
def post_data_table_produtores():
        body = {'nome': 'Test Tester',
                'email': 'test@test.com.br',
                'telefone': '41981234567'}

        return requests.post('http://localhost:5000/produtores',json=body).json()

def test_post_data_table_produtores(post_data_table_produtores):

        result = str(post_data_table_produtores)

        expected = "{'status': 'Created'}"

        assert result == expected

@pytest.fixture
def get_data_table_produtores():

        data = requests.get('http://localhost:5000/produtores').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':
                        return requests.get(f"http://localhost:5000/produtores/{line['id']}").json()['data']


def test_get_data_table_produtores(get_data_table_produtores):


        line_id = get_data_table_produtores['id']

        result = get_data_table_produtores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Test Tester', 'telefone': '41981234567'}

        assert result == expected

@pytest.fixture
def put_data_table_produtores():

        body = {'nome': 'Testado'}

        data = requests.get('http://localhost:5000/produtores').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':
                        requests.put(f"http://localhost:5000/produtores/{line['id']}",json=body)
                        return requests.get(f"http://localhost:5000/produtores/{line['id']}").json()['data']


def test_put_data_table_produtores(put_data_table_produtores):

        line_id = put_data_table_produtores['id']

        result = put_data_table_produtores

        expected = {'email': 'test@test.com.br', 'id': line_id, 'nome': 'Testado', 'telefone': '41981234567'}

        assert result == expected

@pytest.fixture
def delete_data_table_produtores():

        data = requests.get('http://localhost:5000/produtores').json()

        data = data['data']

        result = 'deleted'

        for line in data:
                
                if line['nome'] == 'Testado' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':

                        requests.delete(f"http://localhost:5000/produtores/{line['id']}")

                        data = requests.get('http://localhost:5000/produtores').json()

                        data = data['data']

                        for line in data:

                                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                                        line['telefone'] == '41981234567':
                                        result = 'not deleted'

                return result

def test_delete_data_table_produtores(delete_data_table_produtores):
        
        result = delete_data_table_produtores

        expected = 'deleted'

        assert result == expected