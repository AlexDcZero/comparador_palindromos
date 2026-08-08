def es_palindromo():
    texto = input("Introduzca una cadena:")
    # 1. Limpieza de datos
    texto_limpio = texto.lower().replace(" ", "")

    # 2. Inicializar punteros
    inicio = 0
    fin = len(texto_limpio) - 1
    
    # 3. Comparación desde los extremos al centro
    while inicio < fin:
        if texto_limpio[inicio] != texto_limpio[fin]:
            print(f"La cadena {texto} no es un palindromo")
            return False  # Si no coinciden, no es palíndromo

        inicio = inicio + 1  # Avanzar hacia la derecha
        fin = fin - 1        # Retroceder hacia la izquierda
        
    # 4. Si el bucle termina, ¡es un palíndromo!
    print(f"La cadena {texto} es un palindromo!")
    return True

# --- Pruebas ---
es_palindromo()
