# GRUPO: ...

# Desenvolvam o trabalho neste ficheiro.
# Podem criar outros ficheiros e importá-los aqui.

import sys

def ler_produtos(nome_ficheiro):
    produtos={}
    try:
        f=open(nome_ficheiro,"r", encoding="utf-8")
    except OSError:
        print("Erro: não foi possível abrir o ficheiro", nome_ficheiro)
        return None

    f.readline()
    for linha in f:
        linha=linha.rstrip("\n")
        if linha.strip() =="":
            continue
        partes=linha.split("\t")
        if len(partes) !=5:
            print("Linha ignorada (formato errado):", linha)
            continue
        try: 
            codigo=partes[0].strip()
            nome=partes[1].strip()
            categoria=partes[2].strip()
            preco=float(partes[3].replace(",","."))
            stock=int(partes[4])
        except ValueError:
            print("Linha ignorada por inválidos: ", linha)
            continue
        if codigo == "" or preco < 0 or stock < 0:
            print("Linha ignorada (código vazio ou valores negativos):", linha)
            continue
        if codigo in produtos:
            print("Linha ignorada (código repetido):", linha)
            continue
        produtos[codigo]={"nome": nome, "categoria": categoria, "preco":preco, "stock":stock}

    f.close()
    return produtos 

def guardar_produtos(nome_ficheiro, produtos):
    try:
        f=open(nome_ficheiro, "w", encoding="utf-8")
    except OSError:
        print("Erro: não foi possivel abrir ficheiro", nome_ficheiro)
        return False
    f.write("codigo\tnome\tcategoria\tpreco\tstock\n")
    for codigo in produtos:
        p=produtos[codigo]
        f.write(codigo + "\t"+ p["nome"]+ "\t" + p["categoria"]+ "\t" + format(p["preco"], ".2f") + "\t" + str(p["stock"]) + "\n")
    
    f.close()
    return True 

def consultar_produto(produtos, codigo):
    if codigo in produtos:
        p=produtos[codigo]
        print("Código:", codigo,"\n")
        print("Nome:", p["nome"],"\n")
        print("Categoria:", p["categoria"],"\n")
        print("Preço:", format(p["preco"], ".2f"),"\n")
        print("Stock:", p["stock"],"\n")
    else:
        print("Produto não encontrado.")

def adicionar_produto_carrinho(carrinho, produtos, codigo, quantidade):
    if codigo not in produtos:
        print("Produto não encontrado.")
        return False
    p=produtos[codigo]
    if quantidade > p["stock"]:
        print("Quantidade solicitada excede o stock disponível.")
        return False
    if quantidade <= 0:
        print("Quantidade inválida.")
        return False
    if stock <= 0:
        print("Produto fora de stock.")
        return False
    if codigo in carrinho:
        carrinho[codigo] += quantidade
    else:
        carrinho[codigo] = quantidade
    p["stock"] -= quantidade
    print(f"{quantidade} unidade(s) do produto {p['nome']} adicionada(s) ao carrinho.")
    return True

def consultar_carrinho(carrinho, produtos):
    if not carrinho:
        print("O carrinho está vazio.")
        return
    total=0.0
    print("Carrinho de Compras:")
    for codigo in carrinho:
        quantidade=carrinho[codigo]
        p=produtos[codigo]
        subtotal=quantidade * p["preco"]
        total += subtotal
        print(f"Código: {codigo}, Nome: {p['nome']}, Quantidade: {quantidade}, Preço Unitário: {format(p['preco'], '.2f')}, Subtotal: {format(subtotal, '.2f')}")
    print(f"Total a pagar: {format(total, '.2f')}")

def desconto(carrinho, produtos):
    if codigo in carrinho:
        quantidade = carrinho[codigo]
        if quantidade >= 5:
            p = produtos[codigo]
            desconto = p["preco"] * 0.10
            preco_com_desconto = p["preco"] - desconto
            print(f"Desconto aplicado: 10% no produto {p['nome']}. Novo preço: {format(preco_com_desconto, '.2f')}")



def main():
    ...


if __name__ == "__main__":
    main()

