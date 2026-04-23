import random

def create_game() -> int:
    """El humano esconde el pescado en una de las 3 cajas (0, 1 o 2)"""
    return random.choice([0, 1, 2])

def play_change(n: int = 1000) -> float:
    """El gato ve un pepino en otra caja y decide cambiar."""
    wins = 0
    cajas = [0, 1, 2]
    for _ in range(n):
        pescado = create_game()
        eleccion_gato = random.choice(cajas)
        
        opciones_pepino = [c for c in cajas if c != eleccion_gato and c != pescado]
        caja_pepino = random.choice(opciones_pepino)
        
        
        eleccion_final = [c for c in cajas if c != eleccion_gato and c != caja_pepino][0]
        
        if eleccion_final == pescado:
            wins += 1
    return wins / n

def play_stay(n: int = 1000) -> float:
    """El gato se queda en su caja original pase lo que pase."""
    wins = 0
    cajas = [0, 1, 2]
    for _ in range(n):
        pescado = create_game()
        eleccion_gato = random.choice(cajas)
        
        # No importa qué pepino enseñen, el gato no se mueve
        if eleccion_gato == pescado:
            wins += 1
    return wins / n

def main():
    n = 10000
    success_change = play_change(n)
    success_stay = play_stay(n)
    
    print(f"--- Resultados de la Misión Pescado ({n} intentos) ---")
    print(f"Tasa de éxito si el gato CAMBIA: {success_change:.2%}")
    print(f"Tasa de éxito si el gato SE QUEDA: {success_stay:.2%}")

if __name__ == "__main__":
    main()
