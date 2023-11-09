from typing import List, Dict, Any, Optional


class Produtos:
    produtos: List[Dict[str, Any]] = [
        {
            "id": 1,
            "titulo": "Cadeira Gamer",
            "descricao": "Cadeira confortável para fazer live",
            "preco": 1200.00,
        },
        {
            "id": 2,
            "titulo": "Workshop",
            "descricao": "Workshop de deploy",
            "preco": 100.00,
        },
        {
            "id": 3,
            "titulo": "Iphone",
            "descricao": "Iphone 14",
            "preco": 2000.00,
        },
    ]

    id_atual = 3

    def listar(self):
        return self.produtos
