def test_exito(pesquisa):

    pesquisa.get("https://www.saucedemo.com/")

    pesquisa.find_element("id", "user-name").send_keys("visual_user")

    pesquisa.find_element("id", "password").send_keys("secret_sauce")

    acessar = pesquisa.find_element("id", "login-button")

    acessar.click()

    assert "inventory.html" in pesquisa.current_url
