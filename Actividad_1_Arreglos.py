def leer_entero(mensaje, minimo=None, maximo=None):
    """Solicita un numero entero valido dentro de un rango opcional."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"[Aviso] El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"[Aviso] El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("[Error] Entrada invalida. Por favor, ingresa un numero entero.")


def leer_flotante(mensaje, minimo=None):
    """Solicita un numero decimal (float) valido con limite inferior opcional."""
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor <= minimo:
                print(f"[Aviso] El valor debe ser mayor que {minimo}.")
                continue
            return valor
        except ValueError:
            print("[Error] Entrada invalida. Por favor, ingresa un numero valido.")


def agregar_canciones(nombres, artistas, duraciones, popularidades):
    """A) Registra una o mas canciones en las listas paralelas."""
    cantidad = leer_entero("\nCuantas canciones deseas agregar? ", minimo=1)

    for i in range(1, cantidad + 1):
        print(f"\n--- Cancion {i} de {cantidad} ---")
        while True:
            nombre = input("Nombre de la cancion: ").strip()
            if nombre:
                break
            print("[Aviso] El nombre no puede estar vacio.")

        while True:
            artista = input("Artista: ").strip()
            if artista:
                break
            print("[Aviso] El artista no puede estar vacio.")

        duracion = leer_flotante("Duracion en minutos (ej. 3.5): ", minimo=0.0)
        popularidad = leer_entero("Popularidad (1-100): ", minimo=1, maximo=100)

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print(f"\n[OK] Se agregaron {cantidad} cancion(es) correctamente.")


def calcular_promedio_popularidad(popularidades):
    """Calcula el promedio de popularidad de las canciones registradas."""
    return sum(popularidades) / len(popularidades)


def ver_reportes(nombres, artistas, duraciones, popularidades):
    """B) Muestra estadisticas generales de la playlist."""
    if not nombres:
        print("\n[Aviso] Aun no hay canciones registradas en la playlist.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    promedio_pop = calcular_promedio_popularidad(popularidades)

    max_pop = max(popularidades)
    min_pop = min(popularidades)

    mas_populares = [
        f"{nombres[i]} - {artistas[i]} ({popularidades[i]})"
        for i in range(total_canciones)
        if popularidades[i] == max_pop
    ]
    menos_populares = [
        f"{nombres[i]} - {artistas[i]} ({popularidades[i]})"
        for i in range(total_canciones)
        if popularidades[i] == min_pop
    ]

    horas = int(duracion_total // 60)
    minutos_restantes = duracion_total % 60

    print("\n================ REPORTE DE PLAYLIST ================")
    print(f"- Numero total de canciones: {total_canciones}")
    print(
        f"- Duracion total de la playlist: {duracion_total:.2f} min "
        f"({horas}h {minutos_restantes:.1f}m)"
    )
    print(f"- Cancion(es) mas popular(es) [Pop: {max_pop}]:")
    for item in mas_populares:
        print(f"    * {item}")
    print(f"- Cancion(es) menos popular(es) [Pop: {min_pop}]:")
    for item in menos_populares:
        print(f"    * {item}")
    print(f"- Promedio de popularidad: {promedio_pop:.2f}")
    print("=====================================================")


def buscar_canciones(nombres, artistas, duraciones, popularidades):
    """C) Filtra canciones por artista o por rango de popularidad."""
    if not nombres:
        print("\n[Aviso] Aun no hay canciones registradas para buscar.")
        return

    print("\n--- Buscar canciones ---")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    criterio = leer_entero("Elige un criterio (1-2): ", minimo=1, maximo=2)

    indices_coincidentes = []

    if criterio == 1:
        termino = input("Ingresa el nombre del artista a buscar: ").strip().lower()
        if not termino:
            print("[Aviso] Debes ingresar un nombre de artista.")
            return
        indices_coincidentes = [
            i for i, artista in enumerate(artistas) if termino in artista.lower()
        ]
        encabezado = f"Resultados para artista que contiene '{termino}':"
    else:
        p_min = leer_entero("Popularidad minima (1-100): ", minimo=1, maximo=100)
        p_max = leer_entero("Popularidad maxima (1-100): ", minimo=1, maximo=100)
        if p_min > p_max:
            p_min, p_max = p_max, p_min
            print(f"[Info] Rango ajustado automaticamente de {p_min} a {p_max}.")
        indices_coincidentes = [
            i
            for i, pop in enumerate(popularidades)
            if p_min <= pop <= p_max
        ]
        encabezado = f"Resultados con popularidad entre {p_min} y {p_max}:"

    print(f"\n{encabezado}")
    if not indices_coincidentes:
        print("  No se encontraron canciones con ese criterio.")
    else:
        for idx in indices_coincidentes:
            print(
                f"  - {nombres[idx]} | Artista: {artistas[idx]} | "
                f"Duracion: {duraciones[idx]:.2f} min | Popularidad: {popularidades[idx]}"
            )


def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    """D) Genera una playlist con canciones de popularidad superior al promedio."""
    if not nombres:
        print("\n[Aviso] Aun no hay canciones registradas para generar recomendaciones.")
        return

    promedio = calcular_promedio_popularidad(popularidades)
    recomendadas = [
        i for i, pop in enumerate(popularidades) if pop > promedio
    ]

    print("\n============= PLAYLIST RECOMENDADA =============")
    print(f"Promedio de popularidad actual: {promedio:.2f}")
    print("Criterio: Popularidad estrictamente superior al promedio\n")

    if not recomendadas:
        print("No hay canciones con popularidad superior al promedio actual.")
    else:
        for posicion, idx in enumerate(recomendadas, start=1):
            print(
                f"  {posicion}. {nombres[idx]} - {artistas[idx]} "
                f"({duraciones[idx]:.2f} min | Pop: {popularidades[idx]})"
            )
    print("================================================")


def mostrar_menu():
    print("\n=== FESTIVAL PLAYLIST MANAGER ===")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")


def main():
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []

    while True:
        mostrar_menu()
        opcion = leer_entero("Selecciona una opcion (1-5): ", minimo=1, maximo=5)

        if opcion == 1:
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == 2:
            ver_reportes(nombres, artistas, duraciones, popularidades)
        elif opcion == 3:
            buscar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == 4:
            playlist_recomendada(nombres, artistas, duraciones, popularidades)
        elif opcion == 5:
            print("\nExito con el festival. Saliendo del programa...")
            break


if __name__ == "__main__":
    main()