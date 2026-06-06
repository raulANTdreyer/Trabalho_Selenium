from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage
from pages.checkout_page import CheckoutPage


def test_exito(pesquisa):

    login = LoginPage(pesquisa)
    login.abrir()
    login.realizar_login("standard_user", "secret_sauce")

    assert "inventory.html" in pesquisa.current_url


def test_fiasco(pesquisa):

    login = LoginPage(pesquisa)
    login.abrir()
    login.realizar_login("locked_out_user", "secret_sauce")

    texto_falha = login.obter_texto_erro()

    assert "Sorry, this user has been locked out" in texto_falha


def test_adicionar_ao_carrinho(pesquisa):

    login = LoginPage(pesquisa)
    login.abrir()
    login.realizar_login("visual_user", "secret_sauce")

    produtos = ProdutosPage(pesquisa)
    produtos.adicionar_lanterna_bike()

    assert produtos.obter_quantidade_carrinho() == "1"


def test_remover_do_carrinho(pesquisa):

    login = LoginPage(pesquisa)
    login.abrir()
    login.realizar_login("visual_user", "secret_sauce")

    produtos = ProdutosPage(pesquisa)
    produtos.adicionar_lanterna_bike()

    assert produtos.obter_quantidade_carrinho() == "1"

    produtos.remover_lanterna_bike()

    assert produtos.obter_quantidade_carrinho() == ""


def test_fluxo_compra_completo(pesquisa):

    login = LoginPage(pesquisa)
    login.abrir()
    login.realizar_login("standard_user", "secret_sauce")

    produtos = ProdutosPage(pesquisa)
    produtos.adicionar_lanterna_bike()
    produtos.abrir_carrinho()

    checkout = CheckoutPage(pesquisa)
    checkout.clicar_checkout()
    checkout.preencher_dados_cliente("Raul", "Dreyer", "95560000")
    checkout.finalizar_compra()

    assert checkout.obter_mensagem_sucesso() == "Thank you for your order!"
