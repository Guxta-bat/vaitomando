# testsmain/tests.py

import pytest

from main import saudacao, calcular_media


class TestS:
    def test_S_nome_valido(self):
        resultado = S("Maria")
        assert "Maria" in resultado
    def test_S_tipo_invalido(self):
        with pytest.raises(TypeError):
            S(123)


class TestCalcularMedia:
    def test_media_simples(self):
        assert calcular_media([10, 8, 6]) == 8.0
    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])