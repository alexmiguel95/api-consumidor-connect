from app.models.model import Produtores, Consumidores, Produtos


def test_class_produtores():
    produtor = Produtores(
        nome="Alex Miguel",
        email="alex@gmail.com",
        telefone="41997464",
        senha="123456"
    )

    expected = produtor.nome
    result = "Alex Miguel"

    assert result == expected


def test_class_consumidores():
    consumidor = Consumidores(
        nome="Alex Miguel",
        email="alex@gmail.com",
        telefone="41997464",
        senha="123456"
    )

    expected = consumidor.nome
    result = "Alex Miguel"

    assert result == expected


def test_class_produtos():
    produto = Produtos(
        nome="Morango",
        descricao="Morango muito bom",
        link_foto="url",
        link_video="url",
        fk_produtor=1
    )

    expected = produto.nome
    result = "Morango"

    assert result == expected
