from selenium.webdriver.common.by import By


class ProdutosPage:

    def __init__(self, navegador):

        self.navegador = navegador

        self.botao_add_bike_light = (
            By.ID, "add-to-cart-sauce-labs-bike-light")
        self.botao_remove_bike_light = (By.ID, "remove-sauce-labs-bike-light")
        self.container_carrinho = (By.ID, "shopping_cart_container")

    def adicionar_lanterna_bike(self):

        self.navegador.find_element(*self.botao_add_bike_light).click()

    def remover_lanterna_bike(self):

        self.navegador.find_element(*self.botao_remove_bike_light).click()

    def obter_quantidade_carrinho(self):

        try:

            return self.navegador.find_element(*self.container_carrinho).text

        except:

            return ""

    def abrir_carrinho(self):

        self.navegador.find_element(*self.container_carrinho).click()
