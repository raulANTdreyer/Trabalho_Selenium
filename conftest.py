import pytest
from selenium import webdriver

@pytest.fixture
def pesquisa():
    
    navegador = webdriver.Chrome()

    yield navegador

    navegador.quit()