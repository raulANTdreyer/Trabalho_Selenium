from selenium.webdriver.common.by import By


class acesso_da_pagina:

    def __init__(self, navegador):

        self.navegador = navegador

        self.url = "https://www.saucedemo.com/"
        self.cmp_usuario = (By.ID, "user-name")
        self.cmp_senha = (By.ID, "password")
        self.bt_login = (By.ID, "login-button")

    def abrir(self):

        self.navegador.get(self.url)

    def realizar_acesso(self, usuario, senha):

        self.navegador.find_element(*self.cmp_usuario).send_keys(usuario)
        self.navegador.find_element(*self.cmp_senha).send_keys(senha)
        self.navegador.find_element(*self.bt_login).click()
