def es_palindromo(texto):
    # 1. Limpieza de datos
    texto_limpio = texto.lower().replace(" ", "")
    
    # 2. Inicializar punteros
    inicio = 0
    fin = len(texto_limpio) - 1
    
    # 3. Comparación desde los extremos al centro
    while inicio < fin:
        if texto_limpio[inicio] != texto_limpio[fin]:
            return False  # Si no coinciden, no es palíndromo
        
        inicio = inicio + 1  # Avanzar hacia la derecha
        fin = fin - 1        # Retroceder hacia la izquierda
        
    # 4. Si el bucle termina, ¡es un palíndromo!
    return True

# --- Pruebas ---
print(es_palindromo("Anita lava la tina"))  # Salida: True
print(es_palindromo("0110"))                # Salida: True
print(es_palindromo("Python"))               # Salida: False
print(es_palindromo("0000"))