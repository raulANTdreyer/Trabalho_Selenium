from pages.login_page import acesso_da_pgn
from pages.produtos_page import pgn_produtos


def test_exito(pesquisa):

    acesso = acesso_da_pgn(pesquisa)

    acesso.abrir()
    acesso.realizar_acesso("visual_user", "secret_sauce")

    assert "inventory.html" in pesquisa.current_url


def test_fiasco(pesquisa):

    acesso = acesso_da_pgn(pesquisa)

    acesso.abrir()

    acesso.realizar_acesso("locked_out_user", "secret_sauce")

    texto_falha = acesso.obter_txt_erro()
    assert "Sorry, this user has been locked out" in texto_falha


def test_adc_car(pesquisa):

    acesso = acesso_da_pgn(pesquisa)

    acesso.abrir()

    acesso.realizar_acesso("visual_user", "secret_sauce")

    produtos = pgn_produtos(pesquisa)

    produtos.adc_mochila()

    assert produtos.obt_quant_car() == "1"


def test_rmv_car(pesquisa):

    acesso = acesso_da_pgn(pesquisa)

    acesso.abrir()

    acesso.realizar_acesso("visual_user", "secret_sauce")

    produtos = pgn_produtos(pesquisa)

    produtos.adc_mochila()

    assert produtos.obt_quant_car() == "1"

    produtos.rmv_mochila()

    assert produtos.obt_quant_car() == ""
