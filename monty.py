import random

def create_game() -> int:
    """Escoge la caja ganadora de forma aleatoria."""
    return random.choice([1, 2, 3])

def play_change(n: int = 1000) -> float:
    """Estrategia: Cambiar de caja siempre."""
    wins = 0
    caja = [1, 2, 3]
    
    for _ in range(n):
        ganadora = create_game()
        eleccion_inicial = random.choice(caja)
        
        # El presentador elige una puerta para abrir (pista)
        # No puede ser la ganadora ni la que eligió el jugador
        opciones_pista = [p for p in caja if p != ganadora and p != eleccion_inicial]
        pista = random.choice(opciones_pista)
        
        # El jugador cambia a la puerta que queda
        # No es la inicial ni la que abrió el presentador
        opciones_cambio = [p for p in puertas if p != eleccion_inicial and p != pista]
        nueva_eleccion = random.choice(opciones_cambio)
        
        if nueva_eleccion == ganadora:
            wins += 1
            
    return wins / n

def play_stay(n: int = 1000) -> float:
    """Estrategia: Mantener la puerta inicial."""
    wins = 0
    puertas = [1, 2, 3]
    
    for _ in range(n):
        ganadora = create_game()
        eleccion_inicial = random.choice(puertas)
        
        # Aquí no importa la pista, porque el jugador no cambia
        if eleccion_inicial == ganadora:
            wins += 1
            
    return wins / n

def main():
    n_trials = 10000
    success_change = play_change(n_trials)
    success_stay = play_stay(n_trials)
    
    print(f"Resultados tras {n_trials} simulaciones:")
    print(f"Tasa de éxito cambiando: {success_change:.2%}")
    print(f"Tasa de éxito quedándose: {success_stay:.2%}")

if __name__ == "__main__":
    main()
