from pages.base_page import BasePage
from playwright.sync_api import expect


def test_validar_home(page):
    """
    Teste para validar o acesso à página Home
    - acessa a página Home
    - verifica se o título "AutomationExercise" está visível
    """
    print(test_validar_home.__doc__)
    pagina = BasePage(page)
    pagina.acessar_home()
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()


def test_validar_produtos(page):
    """
    Teste para validar o acesso à página Produtos
    - acessa a página Produtos
    - verifica se a imagem com o nome "Website for practice" está visível
    """
    print(test_validar_produtos.__doc__)
    pagina = BasePage(page)
    pagina.acessar_produtos()
    expect(page.get_by_role("img", name="Website for practice")).to_be_visible()


def test_validar_carrinho(page):
    """
    Teste para validar o acesso à página Carrinho
    - acessa a página Carrinho
    - verifica se o texto "Home Shopping Cart" está visível
    """
    print(test_validar_carrinho.__doc__)
    pagina = BasePage(page)
    pagina.acessar_carrinho()
    expect(page.get_by_text("Home Shopping Cartaa")).to_be_visible()


def test_validar_login(page):
    """
    Teste para validar o acesso à página Login/Cadastro
    - acessa a página Login/Cadastro
    - verifica se o título "Login to your account" está visível
    """
    print(test_validar_login.__doc__)
    pagina = BasePage(page)
    pagina.acessar_cadastro_login()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
