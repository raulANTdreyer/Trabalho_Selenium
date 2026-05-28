from selenium.webdriver.common.by import By


class pgn_produtos:

    def __init__(self, navegador):

        self.navegador = navegador

        self.btn_add_bike_lig = (By.ID, "add-to-cart-sauce-labs-bike-light")

        self.shopp_cntner = (By.ID, "shopping_cart_container")

        self.btn_rmv_bike_lig = (By.ID, "remove-sauce-labs-bike-light")

    def adc_mochila(self):

        self.navegador.find_element(*self.btn_add_bike_lig).click()

    def rmv_mochila(self):

        self.navegador.find_element(*self.btn_rmv_bike_lig).click()

    def obt_quant_car(self):

        try:

            return self.navegador.find_element(*self.shopp_cntner).text

        except:

            return "0"