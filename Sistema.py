def venda_de_produto():
    print("Sistema de Vendas")
    print("-" * 30)

    try:
        produto = input("Produto: ")
        preco = float(input("Preço (R$): "))
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida. Use números válidos.")
        return

    total = preco * qtd
    print(f"\n{qtd}x {produto} a R$ {preco:.2f} cada")
    print(f"Total: R$ {total:.2f}")

    print("\nForma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")
    print("3 - Cartão")

    opcao = input("Opção: ")
    if opcao == "1":
        print("Pagamento em dinheiro.")
    elif opcao == "2":
        print("Pagamento via Pix.")
    elif opcao == "3":
        print("Pagamento com cartão.")
    else:
        print("Opção inválida.")

# Rodar o programa
venda_de_produto()