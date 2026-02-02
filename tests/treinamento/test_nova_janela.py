def test_nova_janela(page):
    # Navegar para a página inicial
    page.goto("https://demoqa.com/browser-windows")
    page.pause()
    page.locator("#windowButton").click()
    page.locator("#windowButton").click()
    page.locator("#windowButton").click()
    page.wait_for_timeout(2000)

    context = page.context
    nova_janela = context.pages[3]

    nova_janela.screenshot(path="tests/treinamento/screenshots/nova_janela2.png")
    nova_janela.close()