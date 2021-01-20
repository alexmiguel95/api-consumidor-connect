from app.models.model import Consumidores


def get_consumidor(email: str):
    """
    Retorna o primeiro consumidor encontrado com o email especificado.
    Caso não encontre nenhum produtor com o email especificado, retorna None.
    """
    return Consumidores.query.filter_by(email=email).first()
