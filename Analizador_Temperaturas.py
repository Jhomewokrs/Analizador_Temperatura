def obtener_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
    return temperaturas


def calcular_promedio(lista):
    return sum(lista) / len(lista)


def encontrar_max_min(lista):
    max_temp = max(lista)
    min_temp = min(lista)
    max_dia = lista.index(max_temp) + 1
    min_dia = lista.index(min_temp) + 1
    return max_temp, max_dia, min_temp, min_dia


def mostrar_alertas(lista):
    alertas = []
    for temp in lista:
        if temp > 40:
            alertas.append(f"Temperatura extrema {temp}°C (mayor a 40°C).")
        elif temp < 0:
            alertas.append(f"Temperatura extrema {temp}°C (menor a 0°C).")
    return alertas


def main():
    print("Programa de análisis de temperaturas semanales.\n")
    temperaturas = obtener_temperaturas()

    max_temp, max_dia, min_temp, min_dia = encontrar_max_min(temperaturas)
    promedio = calcular_promedio(temperaturas)
    alertas = mostrar_alertas(temperaturas)

    print("\n--- Resultados ---")
    print(f"Temperatura máxima: {max_temp}°C (Día {max_dia})")
    print(f"Temperatura mínima: {min_temp}°C (Día {min_dia})")
    print(f"Promedio semanal: {promedio:.2f}°C")
    print("Días con temperatura por encima del promedio:")
    for i, temp in enumerate(temperaturas):
        if temp > promedio:
            print(f"  - Día {i+1}: {temp}°C")
    if alertas:
        print("\nAlertas:")
        for alerta in alertas:
            print(f"  - {alerta}")
    else:
        print("No hubo temperaturas extremas.")


if __name__ == "__main__":
    main()