def best_fit(mem_avail, req_size, index):

    if not mem_avail:
        return None


    if isinstance(req_size, int):
        req_size = [req_size]

    mem_avail = mem_avail[:]
    resultados = []

    for proceso in req_size:
        tamañoProceso = proceso
        best_index = -1  
        best_fit_size = float('inf')

        n = len(mem_avail)
        recorrido = 0 


        i = index
        while recorrido < n:
            base, limite = mem_avail[i]

            if limite >= tamañoProceso and limite < best_fit_size:
                best_index = i
                best_fit_size = limite

            i = (i + 1) % len(mem_avail)
            recorrido += 1

        if best_index == -1:
            return None

        base, limite = mem_avail[best_index]

        nueva_base = base

        nuevo_limite = limite - tamañoProceso 

        if nuevo_limite == 0:
            print(f"Se elimina el bloque {hex(base)} porque quedó completamente asignado")
            del mem_avail[best_index]

            if len(mem_avail) > 0:
                best_index = best_index % len(mem_avail)
            else:
                best_index = 0
        else:
            print(f"Se guarda en el bloque {hex(base)} ")
            mem_avail[best_index] = (base + tamañoProceso, nuevo_limite)

        nuevo_indice = best_index

        resultados.append((mem_avail[:], nueva_base, tamañoProceso, nuevo_indice))

    return resultados[0] if len(resultados) == 1 else resultados

if __name__ == '__main__':
    print("\n Prueba manual:")
    memoria_prueba = [
        (0x06D01000, 0x00500000),
        (0x06100C00, 0x00C00000),
        (0x05200400, 0x00F00000),
        (0x04800000, 0x00A00000),
        (0x01E00000, 0x00400000),
        (0x02500000, 0x01400000),
        (0x07201800, 0x01200000),
        (0x08402C00, 0x00700000)
    ]
    req_prueba = [0x00C00000, 0x00A00000, 0x00B00000]
    index_prueba = 0

    print(f"Memoria antes de asignar: {memoria_prueba}")
    resultado_prueba = best_fit(memoria_prueba, req_prueba, index_prueba)
    print(f"Resultado de best_fit: {resultado_prueba}")
