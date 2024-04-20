import pytest

from basic_excersises import superposicion

def test_superpocion(lista1, lista2):
    expected = True
    assert superposicion(lista1, lista2) == expected
