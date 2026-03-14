continuar = "s"
vendas_do_dia = []

while continuar.lower().startswith("s"):
    valor = float(input("\nValor da Compra: R$ "))
    forma = input("Escolha a forma de Pagamento (1 - Pix, 2 - Débito, 3 - Crédito): ")

    valor_final = 0

    if forma == "1":
        valor_final = valor * 0.85
        print(f"Sua compra teve 15% de desconto.")
        print(f"Valor Total: R$ {valor_final:.2f}")

    elif forma == "2":
        valor_final = valor * 0.95
        print(f"Sua compra teve 5% de desconto.")
        print(f"Valor Total: R$ {valor_final:.2f}")

    elif forma == "3":
        parcelas = int(input("Quantas parcelas? "))

        if parcelas == 1:
            valor_final = valor
            print(f"Pagamento no crédito à vista.")
            print(f"Valor Total: R$ {valor_final:.2f}")

        elif parcelas > 1:
            total_com_juros = valor * 1.10
            valor_parcela = total_com_juros / parcelas
            valor_final = total_com_juros

            print(f"Compra parcelada com 10% de juros.")
            print(f"Total com juros: R$ {total_com_juros:.2f}")
            print(f"{parcelas}x de R$ {valor_parcela:.2f}")

        else:
            print("Número de parcelas inválido.")
            valor_final = 0

    else:
        print("Opção inválida.")
        valor_final = 0

    vendas_do_dia.append(valor_final)

    continuar = input("\nDeseja realizar outra venda? (s/n) ")

print("\n" + "="*30)
print("       RELATORIO DO DIA  ")
print("="*30)
print(f"Total de vendas realizadas: {len(vendas_do_dia)}")
print(f"Faturamento Total: R$ {sum(vendas_do_dia):.2f}")
print(f"Media por venda: R$ {sum(vendas_do_dia)/len(vendas_do_dia) if vendas_do_dia else 0:.2f}")      
print("Caixa fechado. Até amanhã!")
