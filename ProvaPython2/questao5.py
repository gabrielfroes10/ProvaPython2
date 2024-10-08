
def criar_produto(nome, codigo, preco, estoque):
    return (nome, codigo, preco, estoque)


def atualizar_estoque(produto, quantidade):
    nome, codigo, preco, estoque = produto
    novo_estoque = estoque + quantidade
    return (nome, codigo, preco, novo_estoque)


def listar_produtos(produtos):
    for produto in produtos:
        nome, codigo, preco, estoque = produto
        print(f"Produto: {nome}, Código: {codigo}, Preço: R${preco:.2f}, Estoque: {estoque}")


if __name__ == "__main__":
   
    produto1 = criar_produto("Camiseta", 101, 49.90, 20)
    produto2 = criar_produto("Calça Jeans", 102, 89.90, 15)
    produto3 = criar_produto("Tênis", 103, 199.90, 10)

  
    produtos = [produto1, produto2, produto3]

    produto1_atualizado = atualizar_estoque(produto1, 5)
    
  
    produtos[0] = produto1_atualizado

  
    listar_produtos(produtos)
