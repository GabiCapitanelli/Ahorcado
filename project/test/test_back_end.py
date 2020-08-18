import pytest
from project.ahorcado import Ahorcado

def test_prueba():
    a = Ahorcado
    dif = 2
    a.carga_dificultad(a,dif)
    actual = a.devuelve_dificultad(a)
    expected = dif
    assert expected == actual

#Pruebo largo de una palabra
def  test_largo_palabra():
    a = Ahorcado
    actual = a.largo_palabra(a, 'Gato')
    expected = 6
    assert expected == actual

#Pruebo guia 
def test_letra_existe():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.crea_guia(a,'CHAPA')
    actual = a.ingresa_letra_obj(a,'A')
    expected = '**A*A'
    assert expected == actual

def test_puntaje_acierto_dif3():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.dificultad = 3
    actual = a.dev_puntaje_obj(a,8)
    expected = 150
    assert expected == actual

def test_puntaje_acierto_dif2():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.dificultad = 2
    actual = a.dev_puntaje_obj(a,8)
    expected = 100
    assert expected == actual

def test_caracteres_a_insertar():
    a = Ahorcado
    a.limpiar_variables_total(a)
    actual = a.crea_guia(a,'CHAPA')
    expected = '*****'
    assert expected == actual

def test_intentos_restantes():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.crea_guia(a,'CHAPA')
    actual = a.get_intentos(a)
    a.ingresa_letra_obj (a, 'B')
    expected = a.get_intentos(a)
    assert actual == expected + 1

def test_ingresa_alias():
    a = Ahorcado
    actual =  a.ingresa_alias(a,'aLiAs')    
    expected = 'ALIAS'
    assert actual == expected

def test_cambio_puntaje():
    a = Ahorcado
    a.limpiar_variables_total(a)
    a.dificultad = 2
    actual = a.dev_puntaje_obj (a, 3)
    expected = 24
    assert actual == expected
