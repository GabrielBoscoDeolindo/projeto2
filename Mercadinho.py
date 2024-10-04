stock_arroz = stock_feijao = stock_carne = stock_batata = stock_melancia = stock_abacate = stock_banana = stock_leite = stock_miojo = stock_pao = 25
conta = 0
produto = ""

while True:
    itens = int(input("[1] Arroz: R$35,00 \n[2] Feijão: R$25,00 \n[3] Carne: R$25,00 \n[4] Batata: R$5,00 \n[5] Melancia: R$8,00 \n[6] Abacate: R$4,50 \n[7] Banana: R$1,50 \n[8] Leite: R$4,50 \n[9] Miojo: R$2,00 \n[10] Pão: R$0,50 \nQual item deseja comprar: "))
    match itens: 
            case 1:
                arroz = 35.00
                qtd_arroz = int(input("Quantos deseja comprar?: "))
                if qtd_arroz > stock_arroz:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_arroz = stock_arroz - qtd_arroz
                    conta += (arroz*qtd_arroz)
                    produto += "\nArroz - R$ 35.00"
            case 2:
                feijao =  25.00
                qtd_feijao = int(input("Quantos deseja comprar?: "))
                if qtd_feijao > stock_feijao:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_feijao = stock_feijao - qtd_feijao
                    conta += (feijao*qtd_feijao)
                    produto += "\nFeijao - R$25.00"
            case 3:
                carne =  25.00
                qtd_carne = int(input("Quantos deseja comprar?: "))
                if qtd_carne > stock_carne:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_carne = stock_carne - qtd_carne
                    conta += (carne*qtd_carne)
                    produto += "\nCarne - R$25.00"
            case 4:
                batata =  5.00
                qtd_batata = int(input("Quantos deseja comprar?: "))
                if qtd_batata > stock_batata:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_batata = stock_batata - qtd_batata
                    conta += (batata*qtd_batata)
                    produto += "\nBatata - R$5.00"
            case 5:
                melancia =  8.00
                qtd_melancia = int(input("Quantos deseja comprar?: "))
                if qtd_melancia > stock_melancia:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_melancia = stock_melancia - qtd_melancia
                    conta += (melancia*qtd_melancia)
                    produto += "\nMelancia - R$8.00"
            case 6:
                abacate =  4.50
                qtd_abacate = int(input("Quantos deseja comprar?: "))
                if qtd_abacate > stock_abacate:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_abacate = stock_abacate - qtd_abacate
                    conta += (abacate*qtd_abacate)
                    produto += "\nAbacate - R$4.50"
            case 7:
                banana =  1.50
                qtd_banana = int(input("Quantos deseja comprar?: "))
                if qtd_banana > stock_banana:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_banana = stock_banana - qtd_banana
                    conta += (banana*qtd_banana)
                    produto += "\nBanana - R$1.50" 
            case 8:
                leite =  4.50
                qtd_leite = int(input("Quantos deseja comprar?: "))
                if qtd_leite > stock_leite:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_leite = stock_leite - qtd_leite
                    conta += (leite*qtd_leite)  
                    produto += "\nLeite - R$4.50"
            case 9:
                miojo =  2.00
                qtd_miojo = int(input("Quantos deseja comprar?: "))
                if qtd_miojo > stock_miojo:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_miojo = stock_miojo - qtd_miojo
                    conta += (miojo*qtd_miojo) 
                    produto += "\nMiojo - R$2.00"
            case 10:
                pao =  0.50
                qtd_pao = int(input("Quantos deseja comprar?: "))
                if qtd_pao > stock_pao:
                    print("Não temos produtos suficientes em stock!")
                    continue
                else:   
                    stock_pao = stock_pao - qtd_pao
                    conta += (pao*qtd_pao)    
                    produto += "\nPao - R$0.50"
            case _:
                print("Esse item não é válido")
                continue
    duvida = input("Deseja comprar mais alguma coisa?: ")
    if duvida in ["Sim", "sim", "s"]:
        continue
    else:
        break
arquivo = open("notafiscal.txt", "w+")  
print("---------------------------", file=arquivo)
print("Voce deve pagar: R$%.2f" % conta, file=arquivo)
print(f"{produto}", end="\n", file=arquivo) 
print("---------------------------", file=arquivo)
print(f"\nEstoque restante do arroz: {stock_arroz}\nEstoque restante do feijao: {stock_feijao}\nEstoque restante da carne: {stock_carne}\nEstoque restante da batata: {stock_batata}\nEstoque restante do melancia: {stock_melancia}\nEstoque restante do abacate: {stock_abacate}\nEstoque restante da banana: {stock_banana}\nEstoque restante do leite: {stock_leite}\nEstoque restante do miojo: {stock_miojo}\nEstoque restante do pao: {stock_pao}", file=arquivo)





