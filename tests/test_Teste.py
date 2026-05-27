from pages.login_page import acesso_da_pagina


def test_exito(pesquisa):

    acesso = acesso_da_pagina(pesquisa)

    acesso.abrir()
    acesso.realizar_acesso("visual_user", "secret_sauce")

    assert "inventory.html" in pesquisa.current_url


def test_fiasco(pesquisa):

    acesso = acesso_da_pagina(pesquisa)

    acesso.abrir()

    acesso.realizar_acesso("locked_out_user", "secret_sauce")

    texto_falha = acesso.obter_txt_erro()
    assert "Sorry, this user has been locked out" in texto_falha
