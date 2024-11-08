def main():
    characters = []  # Lista para armazenar os personagens

    # Este comando solicita os dados de três personagens
    for i in range(3):
        nome = input("Nome: ")
        ataque = int(input("Ataque: "))
        defesa = int(input("Defesa: "))
        characters.append([nome, (ataque, defesa)])

    #  Este exibe a estrutura criada
    print(characters)

    # Determina os valores máximos de ataque e defesa
    max_ataque = max(characters, key=lambda x: x[1][0])
    max_defesa = max(characters, key=lambda x: x[1][1])

    # E por último exibe os resultados
    print(f"Ataque {max_ataque[0]} {max_ataque[1][0]}")
    print(f"Defesa {max_defesa[0]} {max_defesa[1][1]}")

if __name__ == "__main__":
    main()
