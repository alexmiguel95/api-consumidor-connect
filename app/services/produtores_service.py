from app.models.model import Produtores


def get_produtor(email: str):
    """
    Retorna o primeiro produtor encontrado com o email especificado.
    Caso não encontre nenhum produtor com o email especificado, retorna None.
    """
    return Produtores.query.filter_by(email=email).first()
