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
            stock=float(partes[4])
        except ValueError:
            print("Linha ignorada por inválidos: ", linha)
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



def main():
    ...


if __name__ == "__main__":
    main()

