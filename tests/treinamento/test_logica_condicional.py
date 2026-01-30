from pages.produtos import Produtos


def test_adicionar_produto_ao_carrinho_menor_que_500(page):
    produtos = Produtos(page)
    produtos.acessar_produtos()
    # preco_produto = int(produtos.card_produtos.nth(1).locator(".productinfo h2").inner_text().replace("Rs.", ""))
    preco_produto = int(produtos.card_produtos.nth(2).locator(".productinfo h2").inner_text().replace("Rs.", ""))
    print(f"\n{preco_produto}")
    print(f"{type(preco_produto)}")
    if preco_produto <= 500:
        produtos.adicionar_produto_ao_carrinho(indice_produto=1)
        print("O preço do produto é menor ou igual que 500. Produto adicionado ao carrinho.")
    else:
        print("O preço do produto é maior a 500, produto não adicionado ao carrinho.")
    page.pause()