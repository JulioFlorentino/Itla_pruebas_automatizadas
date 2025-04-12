import pytest
from Test_Web_ITLA import ITLAWebTest  

@pytest.fixture

def test_instance():
    test = ITLAWebTest()
    yield test
    test.cerrar() 
    
def test_busqueda(test_instance):
    test_instance.buscar()

def test_carreras(test_instance):
    test_instance.click_carreras()

def test_extensiones(test_instance):
    test_instance.click_extensiones()

def test_navbar(test_instance):
    test_instance.test_navbar()

def test_chatbot(test_instance):
    test_instance.test_chatbot()
