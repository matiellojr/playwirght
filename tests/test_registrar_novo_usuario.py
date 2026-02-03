from pages.inscreverse import Inscreverse
from playwright.sync_api import expect


def test_registrar_novo_usuario(page):
    inscrever = Inscreverse(page)
    inscrever.acessar_home()
    inscrever.botao_cadastro_login.click()
    expect(page.get_by_text("New User Signup!", exact=True)).to_be_visible()
    inscrever.realizar_cadastro(nome="user_teste", email="test_user1@teste.com")
    expect(page.get_by_text("Enter Account Information", exact=True)).to_be_visible()
    inscrever.preencher_informacoes_da_conta(
        titulo="Mr",
        nome="user_teste",
        senha="123456",
        data_nascimento="10/10/1990",
        sign_up_for_our_newsletter=True,
        receive_special_offers_from=True,
    )
    page.pause()
    inscrever.preencher_detalhes_de_contato(
        primeiro_nome="user",
        sobrenome="teste",
        empresa="empresa teste",
        endereco="Rua teste, 123",
        endereco_2="Apto 45",
        pais="Canada",
        estado="Estado teste",
        cidade="Cidade teste",
        zipcode="A1B2C3",
        numero_telefone="+1234567890",
    )
    inscrever.botao_criar_conta.click()
    expect(page.get_by_text("Account Created!", exact=True)).to_be_visible()
    page.pause()
    inscrever.botao_continuar.click()
    expect(page.get_by_text("Logged in as user_teste", exact=True)).to_be_visible()
    inscrever.botao_deletar_conta.click()
    expect(page.get_by_text("Account Deleted!", exact=True)).to_be_visible()
    inscrever.botao_continuar_2.click()
    page.pause()
