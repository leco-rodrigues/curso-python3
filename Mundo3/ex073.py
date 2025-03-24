# Tuplas com Times de Futebol:
    # Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
    # Depois mostre:
        # A) Apenas os 5 primeiros colocados.
        # B) Os últimos 4 colocados da tabela.
        # C) Uma lista com os times em ordem alfabética.
        # D) Em que posição na tabela está o time da Vasco da Gama.

# Passo 1: Criar uma tupla com os 20 primeiros colocados
team_rankings: tuple[str, ...] = (
    "Palmeiras", "Atlético Mineiro", "Flamengo", "Fluminense", "Internacional", "Atlético Paranaense",
    "Corinthians", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo", "Ceará", "Fortaleza",
    "Red Bull Bragantino", "Santos", "Coritiba", "Goiás", "Cuiabá", "América Mineiro", "Bahia"
)

# Passo 2: Exibir os 5 primeiros colocados
print("Os 5 primeiros colocados na tabela são:")
print(team_rankings[0:5])

# Passo 3: Exibir os 4 últimos colocados
print("\nOs 4 últimos colocados são:")
print(team_rankings[-4:])

# Passo 4: Exibir em ordem alfabética
print("\nA tabela em ordem alfabética fica:")
print(sorted(team_rankings))

# Passo 5: Exibir a posição da "Vasco da Gama"
print(f"\nO Vasco da Gama está na {team_rankings.index('Vasco da Gama') + 1}ª posição.")

# Passo 6: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [073]
