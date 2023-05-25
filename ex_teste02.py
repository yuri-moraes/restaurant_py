print("Welcome to the Restaurant's Yuri Nogueira de Moraes")

# Inicialize o valor total do pedido como zero
TOTAL = 0

# Crie um dicionário com os códigos, nomes e preços dos produtos
products = {
    100: ("Cachorro-quente", 9.00),
    101: ("Cachorro-quente Duplo", 11.00),
    102: ("X-Egg", 12.00),
    103: ("X-Salada", 13.00),
    104: ("X-Bacon", 14.00),
    105: ("X-Tudo", 17.00),
    200: ("Refrigerante Lata", 5.00),
    201: ("Chá Gelado", 4.00),
}

# Crie uma lista vazia para armazenar os pedidos
orders = []

# Imprima um cabeçalho para a lista de produtos
print("-" * 50)
print("Código\t\tNome\t\t\tValor")
print("-" * 50)

# Imprima cada produto com seu código, nome e preço
for code, (name, price) in products.items():
    print(f"{code}\t\t{name:<25}${price:<25}")

# Imprima um rodapé para a lista de produtos
print("-" * 50)

# Loop para receber os pedidos
while True:
    # Solicite ao usuário o código do produto
    order = int(input("Insira o código do produto desejado: "))

    # Verifique se o código do produto é válido
    if order in products:
        # Adicione o preço do produto selecionado ao valor total do pedido
        price = products[order][1]
        TOTAL += price
        # Adicione o produto selecionado à lista de pedidos
        orders.append(products[order])
    else:
        print("Código inválido!")
        continue

    # Solicite ao usuário a escolha de adicionar mais produtos ou finalizar o pedido
    choice = input("Você deseja adicionar mais um produto no pedido? (S/N): ").upper()

    # Verifique se o usuário deseja adicionar mais produtos ou finalizar o pedido
    if choice == "N":
        print("Finalizando pedido...")
        break
    elif choice != "S":
        print("Opção inválida!")
        break

# Imprima um rodapé para a lista de pedidos
print("-" * 50)

# Imprima o valor total do pedido
print(f"O valor total da compra foi R${TOTAL:.2f}")

# Imprima a lista de pedidos com o nome do produto e o preço
print("Pedidos:")
for order in orders:
    print(f"{order[0]} -> R${order[1]:.2f}")
