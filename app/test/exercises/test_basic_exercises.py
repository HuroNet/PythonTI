from app.excercises.basic_exercises import superposition
import pytest


def test_superposition(lista1, lista2):
    expected = True
    assert superposition(lista1, lista2) == expected
