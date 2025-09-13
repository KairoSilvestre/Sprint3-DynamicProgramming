import random
from datetime import datetime, timedelta

def gerar_dados(qtd_registros=10):
    insumos = [
        "Reagente A",
        "Reagente B",
        "Reagente C",
        "Descartável X",
        "Descartável Y"
    ]
    dados = []

    for _ in range(qtd_registros):
        item = random.choice(insumos)
        quantidade = random.randint(1, 20)
        validade = datetime.now() + timedelta(days=random.randint(1, 365))
        dados.append({
            "insumo": item,
            "quantidade": quantidade,
            "validade": validade
        })
    return dados
