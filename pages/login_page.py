from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, navegador):

        self.navegador = navegador
        self.url = "https://www.saucedemo.com/"

        self.campo_usuario = (By.ID, "user-name")
        self.campo_senha = (By.ID, "password")
        self.botao_login = (By.ID, "login-button")
        self.mensagem_erro = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir(self):

        self.navegador.get(self.url)

    def realizar_login(self, usuario, senha):

        self.navegador.find_element(*self.campo_usuario).send_keys(usuario)
        self.navegador.find_element(*self.campo_senha).send_keys(senha)
        self.navegador.find_element(*self.botao_login).click()

    def obter_texto_erro(self):

        return self.navegador.find_element(*self.mensagem_erro).text