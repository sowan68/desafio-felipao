import random


# BIBLIOTECA DE MONSTROS
class Monstro:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = random.randint(50, 100)
        self.ataque = ataque
        self.xp = random.randint(10000, 15000)


monstros = [
    Monstro("Goblin", 50, 20),
    Monstro("Orc", 80, 25),
    Monstro("Esqueleto", 60, 22),
    Monstro("Lobo", 40, 10),
]


# PERGUNTA INICIAL
pergunta = input(
    "Bem-vindo jovem aventureiro! Nosso reino está sob um ataque agora, "
    "você poderia nos ajudar? "
).strip().lower()


while True:

    if pergunta in ("sim", "s"):
        print("Que bom Jovem! Vá para os campos combater nossos inimigos!")
        break

    elif pergunta in ("nao", "n", "não"):
        print(
            "Vocês não merecem estar no nosso reino. "
            "Guardas! Mandem-os para o calabouço."
        )
        exit()

    else:
        pergunta = input(
            "Responda direito Jovem! Não há tempo para tergiversações! "
        ).strip().lower()


# STATUS DO JOGADOR
hp = 100
xp = 0


# EXPLORAÇÃO + BATALHAS
while True:

    comando = input(
        '\nO que deseja fazer? (digite "explorar"): '
    ).strip().lower()

    if comando == "explorar":

    
        modelo = random.choice(monstros)

    
        monstro = Monstro(
            modelo.nome,
            modelo.hp,
            modelo.ataque
        )

        print(f"\nVocê encontrou um {monstro.nome}!")
        print(f"HP do inimigo: {monstro.hp}")

        # BATALHA
        while hp > 0 and monstro.hp > 0:

            print(f"\nSeu HP: {hp}/100")
            print(f"HP do {monstro.nome}: {monstro.hp}")
            print(f"XP: {xp}")

            acao = input(
                "\nO que deseja fazer? "
                "(atacar, curar): "
            ).strip().lower()

            if acao == "atacar":

                dano = random.randint(20, 30)
                monstro.hp -= dano

                print(f"Você causou {dano} de dano!")

            elif acao == "curar":

                cura = random.randint(30, 50)
                hp += cura

                if hp > 100:
                    hp = 100

                print(f"Você recuperou {cura} de HP!")

            else:

                print("Comando inválido!")
                continue

            # Monstro ataca
            if monstro.hp > 0:

                dano_inimigo = random.randint(monstro.ataque, 50)

                hp -= dano_inimigo

                print(
                    f"O {monstro.nome} atacou e causou "
                    f"{dano_inimigo} de dano!"
                )

        # RESULTADO DA BATALHA
        if hp <= 0:

            print("\nVocê foi derrotado!")
            exit()

        elif monstro.hp <= 0:

            print(f"\nVocê derrotou o {monstro.nome}!")

            xp += monstro.xp

            print(f"Você ganhou {monstro.xp} XP!")
            print(f"XP atual: {xp}")

            # PATENTE
            if xp < 1000:
                patente = "Recruta"

            elif xp <= 2000:
                patente = "Soldado"

            elif xp <= 5000:
                patente = "Sargento"

            elif xp <= 7000:
                patente = "Capitão"

            elif xp <= 8000:
                patente = "Comandante"

            elif xp <= 9000:
                patente = "Lorde"

            elif xp <= 10000:
                patente = "Rei"

            else:
                patente = "Imperador"

            print(f"Seu posto atual: {patente}")

            # FINAL DO JOGO
            if xp >= 10001:

                print("\n🏆 PARABÉNS!")
                print("Você se tornou o IMPERADOR!")
                print("Sua jornada chegou ao fim!")

                exit()

    else:

        print('Não podemos fazer isso no momento! ')