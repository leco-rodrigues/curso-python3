# Tuplas com Times de Futebol:
    # Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
    # Depois mostre:
        # A) Apenas os 5 primeiros colocados.
        # B) Os últimos 4 colocados da tabela.
        # C) Uma lista com os times em ordem alfabética.
        # D) Em que posição na tabela está o time da Vasco da Gama.

# Passo 1: Criar uma tupla com os 20 primeiros colocados
team_rankings: tuple[str, ...] = (
    "Palmeiras", "Atlético Mineiro", "Flamengo", "Fluminense", "Internacional",
    "Atlético Paranaense", "Corinthians", "São Paulo", "Grêmio",
    "Vasco da Gama", "Botafogo", "Ceará", "Fortaleza", "Red Bull Bragantino",
    "Santos", "Coritiba", "Goiás", "Cuiabá", "América Mineiro", "Bahia"
)

print(f"\tTeam Rankings:\n {team_rankings}\n")

# Passo 2: Exibir os 5 primeiros colocados
print("The top five teams are:")
print(team_rankings[0:5])

# Passo 3: Exibir os 4 últimos colocados
print("\nThe bottom four teams are:")
print(team_rankings[-4:])

# Passo 4: Exibir em ordem alfabética
print("\nThe table in alphabetical order is:")
print(sorted(team_rankings))

# Passo 5: Exibir a posição da "Vasco da Gama"
print(f"\nVasco da Gama is in {team_rankings.index('Vasco da Gama') + 1}ª position.")

# Passo 6: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [073]
