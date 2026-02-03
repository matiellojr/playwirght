def test_abrir_nova_aba(page):
    # Navegar para a página inicial
    page.goto("https://demoqa.com/browser-windows")
    page.pause()

    with page.expect_popup() as popup_info:
        page.locator("#tabButton").click()

    nova_aba = popup_info.value
    nova_aba.wait_for_load_state()
    page.pause()
