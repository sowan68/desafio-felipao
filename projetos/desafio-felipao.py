import random


# 1. BIBLIOTECA DE MONSTROS
class Monstro:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = random.randint(50,100)
        self.ataque = random.randint(10,30)
        self.xp = random.randint(500,1500)


monstros = [
    Monstro("Goblin", 50, 10),
    Monstro("Orc", 80, 15),
    Monstro("Esqueleto", 60, 12),
    Monstro("Lobo", 40, 8),
]


# 2. PERGUNTA INICIAL
pergunta = input(
    "Bem-vindo jovem aventureiro! Nosso reino está sob um ataque agora, "
    "você poderia nos ajudar? "
).strip().lower()


while True:

    if pergunta in ("sim", "s"):
        print("Que bom Jovem! Vá para os campos combater nossos inimigos!")
        break

    elif pergunta in ("nao", "n", "não"):
        print("Vocês não merecem estar no nosso reino. Guardas! Mandem-os para o calabouço.")
        exit()

    else:
        pergunta = input(
            "Responda direito Jovem! Não há tempo para tergiversações! "
        ).strip().lower()


# 3. STATUS DO JOGADOR
hp = 100
xp = 0


# 4. EXPLORAÇÃO + BATALHAS
while True:

    comando = input("\nO que deseja fazer? (digite explorar): ").strip().lower()

    if comando == "explorar":

        # Escolhe um monstro aleatório
        monstro = random.choice(monstros)

        print(f"\nVocê encontrou um {monstro.nome}!")
        print(f"HP do inimigo: {monstro.hp}")

        # 5. BATALHA
        while hp > 0 and monstro.hp > 0:

            print(f"\nSeu HP: {hp}/100")
            print(f"HP do {monstro.nome}: {monstro.hp}")
            print(f"XP: {xp}")

            acao = input(
                "\nO que deseja fazer? "
                "(atacar, curar): "
            ).strip().lower()

            if acao == "atacar":

                dano = random.randint(20,30)
                monstro.hp -= dano

                print(f"Você causou {dano} de dano!")

            elif acao == "curar":

                cura = random.randint(10,40)
                hp += cura

                if hp > 100:
                    hp = 100

                print(f"Você recuperou {cura} de HP!")

            else:

                print("Comando inválido!")
                continue

            # Monstro ataca
            if monstro.hp > 0:

                hp -= monstro.ataque

                print(
                    f"O {monstro.nome} atacou e causou "
                    f"{monstro.ataque} de dano!"
                )


        # 6. RESULTADO DA BATALHA
        if hp <= 0:

            print("\nVocê foi derrotado!")
            break

        elif monstro.hp <= 0:

            print(f"\nVocê derrotou o {monstro.nome}!")

            xp += monstro.xp

            print(f"Você ganhou {monstro.xp} XP!")
            print(f"XP atual: {xp}")

    else:

        print("Não podemos fazer isso no momento! (digite ""explorar"")")