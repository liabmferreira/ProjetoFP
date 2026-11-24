# GRUPO: ...

# Desenvolvam o trabalho neste ficheiro.
# Podem criar outros ficheiros e importá-los aqui.

import sys

#variaveis globais
limite_desconto= 5
taxa_desconto=0.10

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
    quantidade_no_carrinho = carrinho.get(codigo, 0)
    if quantidade > p["stock"] - quantidade_no_carrinho:
        print("Quantidade solicitada excede o stock disponível.")
        return False
    if quantidade <= 0:
        print("Quantidade inválida.")
        return False
    if p["stock"] <= quantidade_no_carrinho:
        print("Produto fora de stock.")
        return False
    if codigo in carrinho:
        carrinho[codigo] += quantidade
    else:
        carrinho[codigo] = quantidade
    print(f"{quantidade} unidade(s) do produto {p['nome']} adicionada(s) ao carrinho.")
    return True

def consultar_carrinho(carrinho, produtos):
    if not carrinho:
        print("O carrinho está vazio.")
        return
    total=0.0
    print("Carrinho de Compras:")
    for codigo, quantidade in carrinho.items():
        p=produtos[codigo]
        preco_bruto= p["preco"] * quantidade
        desconto, final=calcular_desconto(preco_bruto, quantidade)
        total += final
        print(f"Código: {codigo}, Nome: {p['nome']}, Quantidade: {quantidade}, Preço Unitário: {format(p['preco'], '.2f')}, Desconto: {format(desconto, '.2f')}, Preço Final: {format(final, '.2f')}")
    print(f"Total a pagar: {format(total, '.2f')}")
    return total

def pagar_carrinho(carrinho, produtos):
    if not carrinho:
        print("O carrinho está vazio. Não há nada a pagar.")
        return

    categorias=[]
    for codigo in carrinho:
        if produtos[codigo]["categoria"] not in categorias:
            categorias.append(produtos[codigo]["categoria"]
    categorias.sort()

    print("Fatura")
    print(f"{'Código':<7} {'Produto':<30} {'Qtd':>5} {'Preço':>8} {'Subtot.':>8} {'Desc.':>8} {'Total':>8}")

    total_bruto=0.0
    total_desc=0.0
    for cat in categorias:
        print()
        print("[" +cat +"]")
        for codigo in carrinho:
            p=produto[codigo]
            if p["categoria"] != cat:
                continue
            quantidade=carrinho[codigo]
            subtotal=p["preco"]*quantidade
            desc=calcular_desconto(p["preco",quantidade]
            total_bruto+=subtotal
            total_desc+=desc
            print(f"{codigo:<7} {p['nome']:<30} {quantidade:>5} {p['preco']:>8.2f} {subtotal:>8.2f} {desc:>8.2f} {subtotal - desc:>8.2f}")

    print(f"{'Subtotal:':<60}{total_bruto:>18.2f}")
    print(f"{'Descontos:':<60}{-total_desc:>18.2f}")
    print(f"{'TOTAL A PAGAR:':<60}{total_bruto - total_desc:>18.2f}")
   
    for codigo in carrinho:
        produtos[codigo]["stock"]-=carrinho[codigo]
    carrinho.clear()
    print("Pagamento concluído.")
    
    

def calcular_desconto(total, quantidade):
    if quantidade >= limite_desconto:
        desconto = total * taxa_desconto
        return desconto, total - desconto
    return 0.0, total

def listar_produtos(produtos):
    print("1 - Ver Todos" )
    print("2 - Filtrar por categoria")
    print("3 - Procurar por nome ")
    print("4 - Por preço máximo")
    print("5 - Ver um produto pelo código")
    op=input("Opção: ").strip()

    lista=[]
    if op=="1":
        for codigo in produtos:
            lista.append(codigo)
    elif op=="2":
        categorias=[]
        for codigo in produtos:
            if produtos[codigo]["categoria"] not in categorias:
                categorias.append(produtos[codigo]["categoria"])
        print("Categorias: ", ", ".join(categorias))
        cat=input("Categorua: ").strip().lower()
        for codigo in produtos:
            if produtos[codigo]["categoria"].lower()==cat:
                lista.append(codigo)
    elif op=="3":
        texto=input("Texto a procurar: ").strip().lower()
        for codigo in produtos:
            if texto in produtos[codigo]["nome"].lower():
                lista.append(codigo)
    elif op=="4":
        try:
            maximo=float(input("Perço máximo: ").replace(",","."))
        except ValueError:
            print("Preço inválido.")
            return 
        for codigo in products:
            if produto[codigo]["preco"] <=maximo:
                lista.append(codigo)
    elif op=="5":
        codigo=input("Código: ").strip()
        consultar_produtos(produtos, codigo)
        return 
    else:
        print("Opção inválida")
        return 
        
    mostar_lista(lista,produtos)

def mostrar_lista(lista, produtos):
    if len(lista)==0:
        print("Nenhum produto encontrado")
        return
     print(f"{'Código':<7} {'Nome':<32} {'Categoria':<18} {'Preço':>7} {'Stock':>6}")
    for codigo in lista_
        p=produtos[codigo]
        print(f"{codigo:<7} {p['nome']:<32} {p['categoria']:<18} {p['preco']:>7.2f} {p['stock']:>6}")


def main():
    if len(sys.argv)>1:
        ficheiro=sys.argv[1]
    else:
        ficheiro="produtos.txt"

    produtos=ler_produtos(ficheiro)
    if produtos is None:
        return 

    carrinho={}

while True:
    print()
    print("===Supermercado===")
    print("1 - Consultar Produtos")
    print("2 - Adicionar Produtos ao carrinho")
    print("3 - Consultar Carrinho")
    print("4 - Pagar")




if __name__ == "__main__":
    main()
