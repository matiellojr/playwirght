def test_baixar_arquivo(page):
    page.goto("https://transfer.it/t/U0SqPpgT2Dxb")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="chromedriver").click()
    download = download_info.value
    # Salva o arquivo baixado em um local específico
    download.save_as(r"C:\python\playwirght\stores\teste_baixar_arquivos\chromedriver.zip")
    # Verifica se o arquivo foi baixado corretamente
    assert download.path() is not None
    page.pause()