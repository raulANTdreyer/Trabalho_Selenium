import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def pesquisa():

    navegador = webdriver.Chrome()

    navegador.maximize_window()

    yield navegador

    navegador.quit()
