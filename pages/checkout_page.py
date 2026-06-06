import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, navegador):
        self.navegador = navegador
        self.wait = WebDriverWait(self.navegador, 20)

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
        # Localiza o primeiro campo, limpa e digita com calma
        campo1 = self.wait.until(
            EC.visibility_of_element_located(self.campo_nome))
        campo1.clear()
        campo1.send_keys(nome)
        time.sleep(0.5)  # Pausa milimétrica para o PC lento processar

        campo2 = self.wait.until(
            EC.visibility_of_element_located(self.campo_sobrenome))
        campo2.clear()
        campo2.send_keys(sobrenome)
        time.sleep(0.5)

        campo3 = self.wait.until(
            EC.visibility_of_element_located(self.campo_cep))
        campo3.clear()
        campo3.send_keys(cep)
        time.sleep(0.5)

        botao = self.wait.until(
            EC.element_to_be_clickable(self.botao_continue))
        botao.click()

        self.wait.until(EC.url_contains("checkout-step-two.html"))

    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.botao_finish)).click()

    def obter_mensagem_sucesso(self):
        return self.wait.until(EC.visibility_of_element_located(self.texto_sucesso)).text
