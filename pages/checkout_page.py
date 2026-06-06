import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, navegador):
        self.navegador = navegador
        self.wait = WebDriverWait(self.navegador, 15)

        self.botao_checkout = (By.ID, "checkout")
        self.campo_nome = (By.ID, "first-name")
        self.campo_sobrenome = (By.ID, "last-name")
        self.campo_cep = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")
        self.botao_finish = (By.ID, "finish")
        self.texto_sucesso = (By.CSS_SELECTOR, ".complete-header")

    def clicar_checkout(self):
        self.wait.until(EC.element_to_be_clickable(
            self.botao_checkout)).click()

    def preencher_dados_cliente(self, nome, sobrenome, cep):

        self.wait.until(EC.visibility_of_element_located(
            self.campo_nome)).send_keys(nome)
        self.navegador.find_element(*self.campo_sobrenome).send_keys(sobrenome)
        self.navegador.find_element(*self.campo_cep).send_keys(cep)

        self.navegador.find_element(*self.botao_continue).click()

        time.sleep(2)

    def finalizar_compra(self):

        self.wait.until(EC.element_to_be_clickable(self.botao_finish)).click()

    def obter_mensagem_sucesso(self):
        return self.wait.until(EC.visibility_of_element_located(self.texto_sucesso)).text
