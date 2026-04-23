import random

def create_game() -> int:
    """Escoge la puerta ganadora"""
    return random.randint(1, 3)

def play_change(n: int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta.
    Regresa la tasa de éxito.
    """
    wins = 0
    for _ in range(n):
        puertas = {1, 2, 3}
        ganadora = create_game()
        eleccion_inicial = random.randint(1, 3)
        
        # El presentador abre una puerta que no es la ganadora ni la del jugador
        puertas_posibles_pista = puertas - {ganadora, eleccion_inicial}
        pista = random.choice(list(puertas_posibles_pista))
        
        # El jugador CAMBIA: su nueva elección no es la inicial ni la pista
        nueva_eleccion = (puertas - {eleccion_inicial, pista}).pop()
        
        if nueva_eleccion == ganadora:
            wins += 1
            
    return wins / n

def play_stay(n: int = 1000) -> float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    wins = 0
    for _ in range(n):
        ganadora = create_game()
        eleccion_inicial = random.randint(1, 3)
        
        # En esta estrategia, no importa la pista, nos quedamos con la inicial
        if eleccion_inicial == ganadora:
            wins += 1
            
    return wins / n

def main():
    # Aumentamos n para mayor precisión estadística
    n_trials = 10000
    success_change = play_change(n_trials)
    success_stay = play_stay(n_trials)
    
    print(f"Probabilidad cambiando: {success_change:.2%}")
    print(f"Probabilidad quedándose: {success_stay:.2%}")

if __name__ == "__main__":
    main()


if "__name__" == "__main__":
    main()
