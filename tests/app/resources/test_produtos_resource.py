import requests
import pytest

@pytest.fixture
def post_data_table_produtos():

        body = {'nome': 'Test Tester',
        'email': 'test@test.com.br',
        'telefone': '41981234567'}

        requests.post('http://localhost:5000/produtores',json=body)

        data = requests.get('http://localhost:5000/produtores').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                        line['telefone'] == '41981234567':

                    body = {'nome': 'Test Tester',
                            'descricao': 'teste produto',
                            'link_foto': 'www.testef.com.br',
                            'link_video': 'www.testev.com.br',
                            'fk_produtores': line['id']}

                    return requests.post('http://localhost:5000/produtos',json=body).json()

def test_post_data_table_produtos(post_data_table_produtos):

        result = str(post_data_table_produtos)

        expected = "{'status': 'Created'}"

        assert result == expected


@pytest.fixture
def get_data_table_produtos():

        data = requests.get('http://localhost:5000/produtos').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Test Tester' and line['descricao'] == 'teste produto' and \
                        line['link_foto'] == 'www.testef.com.br' and line['link_video'] == 'www.testev.com.br':

                        return requests.get(f"http://localhost:5000/produtos/{line['id']}").json()['data']


def test_get_data_table_produtos(get_data_table_produtos):

        line_id = get_data_table_produtos['id']


        result = get_data_table_produtos

        expected = {'id': line_id, 'nome': 'Test Tester', 'descricao': 'teste produto', 'link_foto': 'www.testef.com.br',
                            'link_video': 'www.testev.com.br'}

        assert result == expected

@pytest.fixture
def put_data_table_produtos():

    body = {'nome': 'Testado',
            'descricao': 'produto testado'}


    data = requests.get('http://localhost:5000/produtos').json()

    data = data['data']

    for line in data:
            if line['nome'] == 'Test Tester' and line['descricao'] == 'teste produto' and \
                    line['link_foto'] == 'www.testef.com.br' and line['link_video'] == 'www.testev.com.br':


                requests.put(f"http://localhost:5000/produtos/{line['id']}",json=body)

                return requests.get(f"http://localhost:5000/produtos/{line['id']}").json()['data']


def test_put_data_table_produtos(put_data_table_produtos):

        line_id = put_data_table_produtos['id']

        result = put_data_table_produtos

        expected = {'id': line_id, 'nome': 'Testado', 'descricao': 'produto testado', 'link_foto': 'www.testef.com.br',
                            'link_video': 'www.testev.com.br'}

        assert result == expected
    


@pytest.fixture
def delete_data_table_produtos():

        data = requests.get('http://localhost:5000/produtos').json()

        data = data['data']

        for line in data:
                if line['nome'] == 'Testado' and line['descricao'] == 'produto testado' and \
                        line['link_foto'] == 'www.testef.com.br' and line['link_video'] == 'www.testev.com.br':

                        requests.delete(f"http://localhost:5000/produtos/{line['id']}").json()

                        
                        data = requests.get('http://localhost:5000/produtores').json()

                        data = data['data']

                        for line in data:
                        
                                if line['nome'] == 'Test Tester' and line['email'] == 'test@test.com.br' and \
                                        line['telefone'] == '41981234567':

                                        requests.delete(f"http://localhost:5000/produtores/{line['id']}")

                                        return 'deleted'
                


def test_delete_data_table_produtos(delete_data_table_produtos):

    result = delete_data_table_produtos

    expected = 'deleted'

    assert result == expected

