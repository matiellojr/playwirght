
from pages.base_page import BasePage
from playwright.sync_api import expect

def test_validar_home(page):
    pagina = BasePage(page)
    pagina.acessar_home()
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

def test_validar_produtos(page):
    pagina = BasePage(page)
    pagina.acessar_produtos()
    expect(page.get_by_role("img", name="Website for practice")).to_be_visible()

def test_validar_carrinho(page):
    pagina = BasePage(page)
    pagina.acessar_carrinho()
    expect(page.get_by_text("Home Shopping Cart")).to_be_visible()

def test_validar_login(page):
    pagina = BasePage(page)
    pagina.acessar_cadastro_login()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()




