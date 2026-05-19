import random

opcoes = ["pedra", "papel", "tesoura"]
pontos = 0
placar = 0

while True:
    computador = random.choice(opcoes)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Opção inválida. Digite pedra, papel ou tesoura.")
        continue

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu! :)")
        pontos += 1
    else:
        print("Você perdeu ;-;")
        placar += 1

    print(f"Placar: Jogador {pontos} x Computador {placar}")
    teste = input("Deseja jogar novamente? (s/n): ").lower()
    if teste != "s":
        print("Obrigado por jogar!")
        break