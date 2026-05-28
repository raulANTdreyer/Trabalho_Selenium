from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, navegador):

        self.navegador = navegador

        self.botao_checkout = (By.ID, "checkout")

        self.campo_nome = (By.ID, "first-name")
        self.campo_sobrenome = (By.ID, "last-name")
        self.campo_cep = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")

        self.botao_finish = (By.ID, "finish")

        self.texto_sucesso = (By.CSS_SELECTOR, ".complete-header")

    def clicar_checkout(self):

        self.navegador.find_element(*self.botao_checkout).click()

    def preencher_dados_cliente(self, nome, sobrenome, cep):

        self.navegador.find_element(*self.campo_nome).send_keys(nome)
        self.navegador.find_element(*self.campo_sobrenome).send_keys(sobrenome)
        self.navegador.find_element(*self.campo_cep).send_keys(cep)
        self.navegador.find_element(*self.botao_continue).click()

    def finalizar_compra(self):

        self.navegador.find_element(*self.botao_finish).click()

    def obter_mensagem_sucesso(self):

        return self.navegador.find_element(*self.texto_sucesso).text