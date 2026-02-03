from pages.produtos import Produtos
from pages.carrinho import Carrinho

# def test_adicionar_produto_ao_carrinho_menor_que_500(page):
#     produtos = Produtos(page)
#     produtos.acessar_produtos()
#     preco_produto1 = int(produtos.card_produtos.nth(1).locator(".productinfo h2").inner_text().replace("Rs.", ""))
#     preco_produto2 = int(produtos.card_produtos.nth(2).locator(".productinfo h2").inner_text().replace("Rs.", ""))

#     if preco_produto1 <= 500:
#         produtos.adicionar_produto_ao_carrinho(indice_produto=1)
#         print("O preço do produto é menor ou igual que 500. Produto adicionado ao carrinho.")
#     else:
#         print("O preço do produto é maior a 500, produto não adicionado ao carrinho.")
#     page.pause()


def test_excluir_todos_produtos_do_carrinho(page):
    carrinho = Carrinho(page)
    carrinho.acessar_carrinho()
    page.pause()
    while carrinho.botao_excluir_produto.first.is_visible():
        carrinho.botao_excluir_produto.first.click()
        page.wait_for_timeout(
            1000
        )  # Espera 1 segundo para garantir que o produto seja removido
