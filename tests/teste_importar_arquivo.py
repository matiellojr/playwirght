from playwright.sync_api import expect


def test_importar_arquivo_unico(page):
    page.goto("https://transfer.it/start")
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Adicionar arquivos").click()
    file_chooser = fc_info.value
    file_chooser.set_files(
        r"C:\python\playwirght\stores\teste_importar_arquivo\teste1.txt"
    )
    page.get_by_role("textbox", name="O seu email (opcional)").click()
    page.get_by_role("textbox", name="O seu email (opcional)").fill("teste@mail.com")
    page.wait_for_timeout(10000)  # Espera 10 segundos
    page.get_by_role("button", name="Transferir").click()
    expect(page.get_by_role("heading", name="Concluída!")).to_be_visible(
        timeout=10000
    )  # 10 segundos

    # page.get_by_role("button", name="Criar um link").click()
    # page.get_by_role("textbox", name="Seu e-mail").fill("teste@mail1.com")
    # page.get_by_role("button", name="Obter um link").click()
    # page.pause()

    # expect(page.get_by_text("Seu link está pronto!")).to_be_visible(timeout=30000) #30 segundos
    # page.pause()


def test_importar_arquivo_multiplos(page):
    page.goto("https://transfer.it/start")
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Adicionar arquivos").click()
    file_chooser = fc_info.value
    file_chooser.set_files(
        [
            r"C:\python\playwirght\stores\teste_importar_arquivo\teste1.txt",
            r"C:\python\playwirght\stores\teste_importar_arquivo\teste123.txt",
        ]
    )
    page.get_by_role("textbox", name="O seu email (opcional)").click()
    page.get_by_role("textbox", name="O seu email (opcional)").fill("teste@mail.com")
    page.wait_for_timeout(10000)  # Espera 10 segundos
    page.get_by_role("button", name="Transferir").click()
    expect(page.get_by_role("heading", name="Concluída!")).to_be_visible(
        timeout=10000
    )  # 10 segundos
    page.pause()
